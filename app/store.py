import json
import uuid
from pathlib import Path
import time

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

TOKENS_FILE = DATA_DIR / "tokens.json"

if not TOKENS_FILE.exists():
    TOKENS_FILE.write_text(json.dumps({}))

PROFILES_FILE = DATA_DIR / "profiles.json"

if not PROFILES_FILE.exists():
    PROFILES_FILE.write_text(json.dumps([
        {
            "id": "prof_1",
            "service": "twitter",
            "username": "buffer_demo",
            "timezone": "Europe/Zurich"
        },
        {
            "id": "prof_2",
            "service": "linkedin",
            "username": "buffer-demo-company",
            "timezone": "Europe/Zurich"
        }
    ], indent=2))

import time  # add near imports at top

POSTS_FILE = DATA_DIR / "posts.json"
if not POSTS_FILE.exists():
    POSTS_FILE.write_text(json.dumps({}, indent=2))


def load_posts():
    return json.loads(POSTS_FILE.read_text())


def save_posts(posts):
    POSTS_FILE.write_text(json.dumps(posts, indent=2))


def create_post(post: dict) -> dict:
    posts = load_posts()
    post_id = f"post_{uuid.uuid4().hex[:10]}"
    now = int(time.time())

    stored = {
        "id": post_id,
        "profile_id": post["profile_id"],
        "text": post["text"],
        "scheduled_at": post["scheduled_at"],
        "created_at": now,
    }
    posts[post_id] = stored
    save_posts(posts)
    return stored


def get_post(post_id: str):
    return load_posts().get(post_id)


def load_profiles():
    return json.loads(PROFILES_FILE.read_text())


def load_tokens():
    return json.loads(TOKENS_FILE.read_text())


def save_tokens(tokens):
    TOKENS_FILE.write_text(json.dumps(tokens, indent=2))


def create_token(client_id: str):
    tokens = load_tokens()
    token = f"buf_{uuid.uuid4().hex}"
    tokens[token] = {
        "client_id": client_id,
        "scopes": ["profiles.read", "posts.write", "analytics.read"],
    }
    save_tokens(tokens)
    return token


def get_token(token: str):
    return load_tokens().get(token)