import requests
from _common import BASE_URL, auth_headers, handle_response, DEFAULT_TIMEOUT

def main():
    url = f"{BASE_URL}/profiles"
    resp = requests.get(url, headers=auth_headers(), timeout=DEFAULT_TIMEOUT)
    data = handle_response(resp)

    profiles = data["profiles"]
    print(f"Found {len(profiles)} profile(s):")
    for p in profiles:
        print(f"- {p['id']} ({p['service']}): @{p['username']} [{p['timezone']}]")

if __name__ == "__main__":
    main()