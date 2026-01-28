from fastapi import APIRouter, Depends
from app.auth import require_auth
from app.store import load_profiles

router = APIRouter(tags=["profiles"])

@router.get("/profiles")
def list_profiles(_token=Depends(require_auth)):
    return {"profiles": load_profiles()}