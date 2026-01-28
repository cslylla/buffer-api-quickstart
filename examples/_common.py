import os
import sys
import requests

BASE_URL = os.getenv("BUFFER_BASE_URL", "http://127.0.0.1:8000")
TOKEN = os.getenv("BUFFER_TOKEN")

DEFAULT_TIMEOUT = 10


def auth_headers():
    if not TOKEN:
        print("Missing env var BUFFER_TOKEN", file=sys.stderr)
        sys.exit(1)
    return {"Authorization": f"Bearer {TOKEN}"}


def handle_response(resp: requests.Response):
    try:
        data = resp.json()
    except ValueError:
        data = {"raw": resp.text}

    if resp.status_code >= 400:
        print(f"HTTP {resp.status_code}: {data}", file=sys.stderr)
        sys.exit(1)

    return data