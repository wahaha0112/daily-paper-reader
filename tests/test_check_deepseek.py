import importlib.util
import io
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError

spec = importlib.util.spec_from_file_location('check_deepseek', Path(__file__).resolve().parents[1] / 'src/check_deepseek.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


class PreflightTests(unittest.TestCase):
    def test_valid_model_uses_free_models_endpoint(self):
        with patch.object(c, 'urlopen', return_value=io.BytesIO(b'{"data":[{"id":"deepseek-flash"}]}')) as call:
            self.assertTrue(c.check('fixture-key', 'https://api.deepseek.com', 'deepseek-flash'))
        self.assertEqual(call.call_args[0][0].full_url, 'https://api.deepseek.com/models')

    def test_wrong_endpoint_never_receives_secret(self):
        with patch.object(c, 'urlopen') as call:
            with self.assertRaises(ValueError):
                c.check('fixture-key', 'https://example.com', 'deepseek-flash')
        call.assert_not_called()

    def test_authentication_error_is_sanitized(self):
        error = HTTPError('https://api.deepseek.com/models', 401, 'sensitive-body', {}, None)
        with patch.object(c, 'urlopen', side_effect=error):
            with self.assertRaisesRegex(ValueError, r'HTTP 401') as result:
                c.check('fixture-key', 'https://api.deepseek.com', 'deepseek-flash')
        self.assertNotIn('fixture-key', str(result.exception))
        self.assertNotIn('sensitive-body', str(result.exception))
