// Standalone source extension: leave the upstream sidebar's paper state untouched.
(function () {
  const insert = () => {
    const sidebar = document.querySelector('.sidebar');
    if (!sidebar || document.getElementById('dpr-ccf-entry')) return;
    const a = document.createElement('a');
    a.id = 'dpr-ccf-entry'; a.href = 'ccf.html';
    a.textContent = 'CCF-A 会议与期刊';
    a.style.cssText = 'display:block;margin:12px 18px;padding:10px 12px;border:1px solid #d2e2e4;border-radius:6px;color:#17656f;font-size:14px;text-decoration:none;background:#f2f8f8;';
    sidebar.prepend(a);
  };
  new MutationObserver(insert).observe(document.documentElement, {childList:true, subtree:true});
  insert();
})();
