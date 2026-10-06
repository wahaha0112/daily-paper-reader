(function () {
  'use strict';
  let data, filtered = [], page = 0;
  const size = 30;
  const el = id => document.getElementById(id);
  const node = (tag, text, cls) => { const n = document.createElement(tag); if (text != null) n.textContent = text; if (cls) n.className = cls; return n; };
  const safe = value => { try { const u = new URL(value); return ['https:', 'http:'].includes(u.protocol) && !u.username ? u.href : ''; } catch { return ''; } };
  const link = (label, url) => { const a = node('a', label); a.href = url; return a; };
  function options(id, items) { items.forEach(([value, label]) => { const o = node('option', label); o.value = value; el(id).append(o); }); }
  function filter() {
    const q = el('search').value.trim().toLowerCase();
    filtered = data.papers.filter(p => (!el('related').checked || p.topic_tags.length) &&
      (!el('abstract').checked || p.abstract) && (!el('kind').value || p.kind === el('kind').value) &&
      (!el('venue').value || p.venue_key === el('venue').value) &&
      (!el('topic').value || p.topic_tags.includes(el('topic').value)) &&
      (!q || [p.title, p.abstract, p.doi, ...(p.authors || [])].join(' ').toLowerCase().includes(q)));
    const order = el('sort').value;
    filtered.sort((a, b) => order === 'score'
      ? (b.ai?.score ?? -1) - (a.ai?.score ?? -1)
      : String(order === 'seen' ? b.first_seen : b.publication_date).localeCompare(String(order === 'seen' ? a.first_seen : a.publication_date)));
    page = 0; render();
  }
  function render() {
    el('papers').replaceChildren();
    const pages = Math.max(1, Math.ceil(filtered.length / size));
    el('count').textContent = `${filtered.length} 篇符合当前筛选 · 共 ${data.papers.length} 篇书目 · 未生成 AI 分数的论文不按质量排序`;
    if (!filtered.length) el('papers').append(node('p', '当前筛选没有结果。可以取消“只看方向初筛命中”或更换来源；这不代表该方向没有论文。', 'empty'));
    filtered.slice(page * size, (page + 1) * size).forEach(p => {
      const card = node('article', null, 'paper');
      card.append(node('div', `${p.venue} · ${p.kind === 'journal' ? '期刊' : '会议'} · ${p.publication_date || '日期未知'}${p.date_precision === 'year' ? '（仅年份）' : p.date_precision === 'month' ? '（仅月份）' : ''}`, 'meta'));
      const title = node('h2'); title.append(link(p.title, safe(p.url) || '#')); card.append(title);
      if (p.ai?.title_zh) card.append(node('p', p.ai.title_zh));
      card.append(node('div', (p.authors || []).slice(0, 8).join(', '), 'authors'));
      const badges = node('div');
      p.topic_tags.forEach(t => badges.append(node('span', data.topic_labels[t] || t, 'badge')));
      badges.append(node('span', p.ai ? `AI 相关性 ${p.ai.score}/10 · 基于摘要` : p.abstract ? '有摘要 · 尚未 AI 评审' : '仅书目 · 未提供摘要', 'badge')); card.append(badges);
      if (p.ai) card.append(node('p', p.ai.summary_zh, 'abstract'));
      if (p.abstract) { const d = node('details'); d.append(node('summary', '查看原文摘要'), node('p', p.abstract, 'abstract')); card.append(d); }
      const actions = node('div', null, 'actions');
      actions.append(link('官方论文页面 ↗', safe(p.url) || '#'));
      if (p.topic_tags.length && /^[a-f0-9]{20}$/.test(p.id)) actions.append(link('进入原站阅读页', `./#/ccf/papers/${p.id}`));
      if (safe(p.pdf_url)) actions.append(link('公开 PDF ↗', safe(p.pdf_url)));
      card.append(actions); el('papers').append(card);
    });
    el('page').textContent = `${page + 1} / ${pages}`;
    el('previous').disabled = page === 0; el('next').disabled = page >= pages - 1;
  }
  async function start() {
    try {
      const response = await fetch('docs/ccf/index.json', {cache: 'no-store'});
      if (!response.ok) throw new Error('index_unavailable');
      data = await response.json();
      if (!Array.isArray(data.papers) || !Array.isArray(data.coverage)) throw new Error('invalid_index');
      const failed = data.coverage.filter(v => v.status === 'partial').length;
      el('status').textContent = `最近更新：${new Date(data.updated_at).toLocaleString('zh-CN')} · ${failed ? `${failed} 个来源存在部分失败，保留已有结果。` : '已读取本次公开来源。'} 会议回溯近两年，期刊检索近 120 天（TIFS 仅有年份，保留当年书目）；并非完整收录。`;
      [[data.configured_venues.length, '配置来源'], [data.papers.length, '保留书目'], [data.papers.filter(p => p.topic_tags.length).length, '方向初筛命中'], [data.papers.filter(p => p.ai).length, '已完成 AI 摘要解读']].forEach(([n, label]) => { const d = node('div', null, 'stat'); d.append(node('strong', String(n)), node('span', label)); el('stats').append(d); });
      options('venue', data.configured_venues.map(v => [v.key, v.name])); options('topic', Object.entries(data.topic_labels));
      const table = node('table'), head = node('tr'); ['来源', '状态', '本次返回', '渠道说明'].forEach(t => head.append(node('th', t))); table.append(head);
      const labels = {unavailable:'暂不可用', bounded:'达到检索上限', indexed_query_complete:'已取完该查询的索引结果', official_list:'官方列表已读取'};
      const coverageMap = new Map(data.coverage.map(c => [c.venue_key,c]));
      data.configured_venues.forEach(v => { const c = coverageMap.get(v.key); const row = node('tr'); [v.name, c ? (c.status === 'partial' ? '部分失败 / 待复查' : '查询成功') : '尚未检索', c ? String(c.results) : '—', c ? c.providers.map(p => `${p.provider}${p.year ? ' '+p.year : ''}：${labels[p.status] || p.status}${p.date_note ? '；'+p.date_note : ''}`).join('；') : '无本次证据'].forEach(t => row.append(node('td',t))); table.append(row); });
      el('coverage').append(table);
      ['search','kind','venue','topic','related','abstract','sort'].forEach(id => el(id).addEventListener(id === 'search' ? 'input' : 'change', filter));
      el('previous').onclick = () => {page--; render();}; el('next').onclick = () => {page++; render();};
      el('export').onclick = () => {const blob = new Blob([JSON.stringify({exported_at:new Date().toISOString(),limitations:data.limitations,papers:filtered},null,2)],{type:'application/json'});const url=URL.createObjectURL(blob);const a=link('',url);a.download='ccf-research-papers.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);};
      filter();
    } catch { el('status').classList.add('error'); el('status').textContent = '文献索引尚未发布或读取失败。请到“更新文献”运行免费书目更新后刷新；不会把读取失败显示成 0 篇。'; }
  }
  start();
})();
