from fastapi import Header, HTTPException
from app.store import get_token

def require_auth(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    token = authorization.split(" ")[1]
    token_data = get_token(token)

    if not token_data:
        raise HTTPException(status_code=403, detail="Invalid token")

    return token_data