import importlib.util
import json
import sys
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('ccf_watch', ROOT / 'src/ccf_watch.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
CONFIG = json.loads((ROOT / 'ccf-sources.json').read_text())


class CCFWatchTests(unittest.TestCase):
    def test_catalog_has_all_twenty_three_requested_sources(self):
        venues = CONFIG['venues']
        self.assertEqual(len({v['key'] for v in venues}), 23)
        self.assertEqual(sum(v['kind'] == 'conference' for v in venues), 16)
        self.assertEqual(sum(v['kind'] == 'journal' for v in venues), 7)

    def test_periodical_conference_mapping(self):
        for key, issue, expected in [('fse', 'FSE', True), ('fse', 'ISSTA', False), ('oopsla', 'OOPSLA2', True), ('popl', 'OOPSLA2', False)]:
            provider = next(v for v in CONFIG['venues'] if v['key'] == key)['providers'][0]
            self.assertEqual(c.source_matches({'ISSN': [provider['issn']], 'issue': issue}, provider), expected)

    def test_workshops_and_companion_are_not_main_conferences(self):
        provider = next(v for v in CONFIG['venues'] if v['key'] == 'icse')['providers'][0]
        for title in ['International Conference on Software Engineering Companion', 'International Conference on Software Engineering: Software Engineering in Practice', 'International Conference on Software Engineering Workshops']:
            self.assertFalse(c.source_matches({'container-title': [title]}, provider))
        self.assertTrue(c.source_matches({'container-title': ['Proceedings of the 48th International Conference on Software Engineering']}, provider))

    def test_fse_does_not_mean_fast_software_encryption(self):
        provider = next(v for v in CONFIG['venues'] if v['key'] == 'fse')['providers'][-1]
        self.assertFalse(c.source_matches({'container-title': ['Fast Software Encryption']}, provider))

    def test_journal_matching_requires_issn(self):
        provider = {'issn': '0098-5589'}
        self.assertFalse(c.source_matches({'container-title':['IEEE Transactions on Software Engineering']}, provider))
        self.assertTrue(c.source_matches({'ISSN':['0098-5589']}, provider))

    def test_publication_date_preserves_precision_and_ignores_indexing(self):
        self.assertEqual(c.publication_date({'published':{'date-parts':[[2026,9]]}})[:2], ('2026-09','month'))
        self.assertEqual(c.publication_date({'indexed':{'date-parts':[[2026,9,1]]}})[:2], ('','unknown'))

    def test_invalid_and_future_dates(self):
        self.assertEqual(c.publication_date({'published':{'date-parts':[[2026,99,1]]}})[1], 'unknown')
        item={'title':['A real paper'], 'DOI':'10.1/a','ISSN':['0098-5589'],'published':{'date-parts':[[2030,1,1]]}}
        venue=next(v for v in CONFIG['venues'] if v['key']=='tse')
        self.assertIsNone(c.from_crossref(item,venue,venue['providers'][0],date(2026,10,6)))

    def test_missing_abstract_does_not_become_generated_text(self):
        venue=next(v for v in CONFIG['venues'] if v['key']=='tse')
        item={'title':['A real paper'], 'DOI':'10.1/a','ISSN':['0098-5589']}
        paper=c.from_crossref(item,venue,venue['providers'][0],date(2026,10,6))
        self.assertEqual(paper['content_basis'],'title_only')
        self.assertEqual(paper['abstract'],'')

    def test_skill_does_not_match_motor_skill_acquisition(self):
        self.assertNotIn('skill', c.topic_hits({'title':'Reinforcement Learning for Motor Skill Acquisition'},CONFIG['topic_patterns']))
        self.assertIn('skill', c.topic_hits({'title':'Prompt Injection in LLM Agents'},CONFIG['topic_patterns']))

    def test_no_paid_call_by_default(self):
        paper={'title':'Vulnerability detection','abstract':'Real abstract','topic_tags':['code-vuln']}
        with patch.object(c.requests,'post') as post:
            result=c.review_papers([paper],[],{},0)
        post.assert_not_called()
        self.assertEqual(result['attempted_calls'],0)

    def test_no_title_only_paid_summary(self):
        with patch.object(c.requests,'post') as post:
            c.review_papers([{'title':'Vulnerability detection','topic_tags':['code-vuln']}],[],{},1)
        post.assert_not_called()

    def test_cache_changes_with_abstract_and_profile(self):
        p={'title':'A','abstract':'First'}
        key=c.review_key(p,[],'model')
        self.assertNotEqual(key,c.review_key({**p,'abstract':'Second'},[],'model'))
        self.assertNotEqual(key,c.review_key(p,[{'tag':'new'}],'model'))

    def test_unsafe_url_rejected(self):
        self.assertEqual(c.safe_url('javascript:alert(1)'), '')
        self.assertEqual(c.safe_url('https://secret@example.com/paper'), '')
        self.assertTrue(c.safe_url('https://doi.org/10.1/example'))

    def test_bounded_pagination_is_reported(self):
        class Client:
            def get(self,*args,**kwargs):
                return {'message':{'total-results':5000,'items':[{'title':['No DOI']}], 'next-cursor':'next'}}
        venue=CONFIG['venues'][0]
        papers, status=c.fetch_crossref(Client(),venue,venue['providers'][0],{**CONFIG,'max_pages_per_provider':1},date(2026,10,6))
        self.assertEqual(status['status'],'bounded')
        self.assertFalse(status['exhaustive_venue_coverage'])

    def test_publication_sort_uses_offsets_not_unsupported_cursor(self):
        calls=[]
        class Client:
            def get(self, url, params):
                calls.append(dict(params))
                return {'message':{'total-results':2,'items':[{'title':['No DOI']}]}}
        venue=CONFIG['venues'][0]
        c.fetch_crossref(Client(),venue,venue['providers'][0],CONFIG,date(2026,10,6))
        self.assertEqual([p['offset'] for p in calls],[0,1])
        self.assertTrue(all('cursor' not in p for p in calls))

    def test_electronic_issn_is_matched_when_verified(self):
        provider=next(v for v in CONFIG['venues'] if v['key']=='tifs')['providers'][0]
        self.assertTrue(c.source_matches({'ISSN':['1556-6021']},provider))

    def test_ase_journal_is_not_mislabeled_as_a_conference(self):
        provider=next(v for v in CONFIG['venues'] if v['key']=='ase')['providers'][0]
        self.assertFalse(c.source_matches({'container-title':['Automated Software Engineering']},provider))
        self.assertTrue(c.source_matches({'container-title':['2025 IEEE/ACM 40th International Conference on Automated Software Engineering (ASE)']},provider))

    def test_untrusted_markdown_cannot_inject_links(self):
        self.assertIn(r'\[click\]',c.markdown_text('[click](https://example.com)'))
        self.assertNotIn('<script>',c.markdown_text('<script>alert(1)</script>'))

    def test_changed_abstract_discards_stale_review(self):
        paper={'title':'A','abstract':'Changed','topic_tags':['skill'],'ai':{'score':10}}
        c.review_papers([paper],[],{},0)
        self.assertNotIn('ai',paper)

    def test_defi_does_not_match_defining_or_definitive(self):
        self.assertNotIn('smart-contract',c.topic_hits({'title':'Defining and Verifying Programs'},CONFIG['topic_patterns']))
        self.assertIn('smart-contract',c.topic_hits({'title':'DeFi Scam Detection'},CONFIG['topic_patterns']))

    def test_springer_series_does_not_hide_conference_title(self):
        provider=next(v for v in CONFIG['venues'] if v['key']=='crypto')['providers'][0]
        self.assertTrue(c.source_matches({'container-title':['Lecture Notes in Computer Science','Advances in Cryptology – CRYPTO 2026']},provider))

    def test_fm_uses_verified_book_and_main_track_only(self):
        p=next(v for v in CONFIG['venues'] if v['key']=='fm')['providers'][0]
        self.assertTrue(c.source_matches({'ISBN':[p['isbn']],'DOI':p['doi_prefix']+'3'},p))
        self.assertFalse(c.source_matches({'ISBN':[p['isbn']],'DOI':p['doi_prefix']+'1'},p))
        self.assertFalse(c.source_matches({'ISBN':['9781009421003'],'DOI':p['doi_prefix']+'3'},p))

    def test_reader_frontmatter_is_single_line_and_inline_array(self):
        text=c.render_paper({'title':'A long title: with punctuation','authors':['A','B'], 'venue':'TSE','url':'https://doi.org/10.1/a','topic_tags':['skill']})
        self.assertIn('tags: ["query:skill"]',text)
        self.assertEqual(text.count('\n---'),1)
        self.assertNotIn('\n# A long',text)


if __name__=='__main__':
    unittest.main()
