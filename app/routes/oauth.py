from fastapi import APIRouter, Query, Form
from app.store import create_token

router = APIRouter(prefix="/oauth", tags=["oauth"])

@router.get("/authorize")
def authorize(
    client_id: str = Query(...),
    redirect_uri: str = Query(...),
):
    code = f"code_{client_id}"
    return {
        "code": code,
        "redirect_uri": redirect_uri,
        "message": "User approved application (mock)."
    }

@router.post("/token")
def token(
    client_id: str = Form(...),
    client_secret: str = Form(...),
    code: str = Form(...),
):
    if not code.startswith("code_"):
        return {"error": "invalid_grant"}

    access_token = create_token(client_id)
    return {"access_token": access_token, "token_type": "bearer"}