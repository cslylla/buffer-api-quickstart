import sys
import requests
from _common import BASE_URL, auth_headers, handle_response, DEFAULT_TIMEOUT

def main():
    if len(sys.argv) != 2:
        print("Usage: python examples/get_analytics.py <post_id>")
        sys.exit(1)

    post_id = sys.argv[1]
    url = f"{BASE_URL}/analytics/{post_id}"

    resp = requests.get(url, headers=auth_headers(), timeout=DEFAULT_TIMEOUT)
    data = handle_response(resp)

    m = data["metrics"]
    print(f"Analytics for {data['post_id']}:")
    print(f"- impressions: {m['impressions']}")
    print(f"- clicks: {m['clicks']}")
    print(f"- likes: {m['likes']}")
    print(f"- engagement_rate: {m['engagement_rate']}")

if __name__ == "__main__":
    main()