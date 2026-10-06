"""Fail early on invalid official DeepSeek credentials; never generate paid text."""
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


def check(api_key, base_url, model):
    if not api_key:
        raise ValueError('DEEPSEEK_API_KEY is missing')
    base = base_url.rstrip('/')
    parsed = urlsplit(base)
    if parsed.scheme != 'https' or parsed.hostname != 'api.deepseek.com' or parsed.username or parsed.port not in (None, 443):
        raise ValueError('Official DeepSeek HTTPS endpoint required')
    request = Request(base + '/models', headers={'Authorization': 'Bearer ' + api_key})
    try:
        with urlopen(request, timeout=20) as response:
            result = json.load(response)
    except HTTPError as exc:
        raise ValueError(f'DeepSeek authentication/model preflight failed (HTTP {exc.code})') from None
    except (URLError, TimeoutError, OSError, ValueError):
        raise ValueError('DeepSeek preflight could not reach or read the official API') from None
    if model not in {m.get('id') for m in result.get('data', []) if isinstance(m, dict)}:
        raise ValueError('Configured model is absent from the official model list')
    return True


if __name__ == '__main__':
    try:
        check(os.getenv('DEEPSEEK_API_KEY'), os.getenv('DEEPSEEK_BASE_URL', 'https://api.deepseek.com'),
              os.getenv('DEEPSEEK_MODEL', 'deepseek-flash'))
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
    print('DeepSeek authentication and model preflight passed; no text generation requested.')
