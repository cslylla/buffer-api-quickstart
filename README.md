# Buffer API Quickstart (Mock)

A tiny, polished **developer quickstart** that simulates a minimal Buffer-style API workflow:
- Connect via OAuth (mocked)
- List connected social profiles
- Schedule a post
- Fetch post status
- Read basic analytics (mocked + deterministic)

This is a **DX/demo project** (not a production integration) designed as a portfolio project.

---

## Overview

### Who this is for
- Developers who want to see a clean “starter kit” style integration
- Developer Advocates / API teams evaluating onboarding + docs quality

## What you get
- FastAPI mock server with realistic endpoints
- Mock OAuth flow (offline)
- JSON persistence for tokens + posts
- Example scripts that mirror real integration tasks
- Postman collection for instant exploration

---

## Quickstart

### 1) Clone + install
```
git clone https://github.com/<your-username>/buffer-api-quickstart.git
cd buffer-api-quickstart

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

### 2) Start the API
```
uvicorn app.main:app --reload
```
Verify the app is running:
```
curl http://127.0.0.1:8000/health
```

### 3) API Authentication
This project uses a mock OAuth 2.0-style flow.

#### Step A — Authorize
```
curl "http://127.0.0.1:8000/oauth/authorize?client_id=demo_client&redirect_uri=http://localhost"
```
Response includes a code (mocked).

#### B — Exchange code for a token
```
curl -X POST http://127.0.0.1:8000/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=demo_client" \
  -d "client_secret=demo_secret" \
  -d "code=code_demo_client"
```
Use the returned token like:
```
Authorization: Bearer buf_...
```

#### Environment variables (for scripts)
```
export BUFFER_BASE_URL="http://127.0.0.1:8000"
export BUFFER_TOKEN="buf_..."
```

## Example Workflows
### 1) List connected profiles

```
python examples/list_profiles.py
```

### 2) Schedule a post
```
python examples/schedule_post.py
```

### 3) Fetch analytics for a post
```
python examples/get_analytics.py <post_id>
```

## API Endpoints

| Method | Endpoint            | Description                   |
|--------|---------------------|-------------------------------|
| GET    | `/health`           | Service health check          |
| GET    | `/oauth/authorize`  | Mock OAuth authorization      |
| POST   | `/oauth/token`      | Exchange code for access token|
| GET    | `/profiles`         | List connected social profiles|
| POST   | `/posts`            | Schedule a post               |
| GET    | `/posts/{id}`       | Retrieve post status          |
| GET    | `/analytics/{id}`   | Fetch post analytics          |

## Postman Collection
### File
A ready-to-use Postman collection is included.
```
postman/buffer-quickstart.json
```

### Collection variables
- `base_url` — API base URL
- `access_token` — OAuth access token
- `post_id` — Auto-populated after creating a post
The Create Post request automatically saves `post_id` for subsequent requests.

## Troubleshooting
### 401 Missing Authorization header
You did not send:
```
Authorization: Bearer <token>
```

### 403 Invalid token
The token is not present in data/tokens.json or is outdated.

### 404 Profile not found
POST /posts requires a valid profile_id from GET `/profiles`.

### 422 Validation error
The request body is missing required fields or has invalid types.
Inspect the response for field-level errors.

## Developer Experience Notes
This project intentionally mirrors real-world API onboarding patterns:
- Deterministic mock analytics (same `post_id` → same metrics)
- Local JSON persistence (data/*.json) so the demo survives restarts
- Clear separation between API, examples, and tooling
- Minimal but realistic endpoint surface area

## Next Steps / Roadmap
Possible extensions for a production-ready starter kit:
- OAuth scopes + per-endpoint enforcement
- Pagination for list endpoints
- Idempotency keys for POST `/posts`
- Webhook simulation for post lifecycle events
- Tiny UI walkthrough for first-time developers

## License
MIT