import time
import requests
from _common import BASE_URL, auth_headers, handle_response, DEFAULT_TIMEOUT

def main():
    url = f"{BASE_URL}/posts"

    payload = {
        "profile_id": "prof_1",
        "text": "Hello from examples/schedule_post.py",
        "scheduled_at": int(time.time()) + 3600,
    }

    resp = requests.post(url, json=payload, headers=auth_headers(), timeout=DEFAULT_TIMEOUT)
    data = handle_response(resp)

    post = data["post"]
    print("Scheduled post:")
    print(f"- id: {post['id']}")
    print(f"- status: {post['status']}")
    print(f"- scheduled_at: {post['scheduled_at']}")
    print(f"- text: {post['text']}")

if __name__ == "__main__":
    main()