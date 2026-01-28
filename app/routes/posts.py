import time
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from app.auth import require_auth
from app.store import create_post, get_post, load_profiles

router = APIRouter(tags=["posts"])


class PostCreate(BaseModel):
    profile_id: str = Field(..., examples=["prof_1"])
    text: str = Field(..., min_length=1, max_length=280)
    scheduled_at: int = Field(..., description="Unix timestamp (seconds)")


def compute_status(post: dict) -> str:
    now = int(time.time())
    if post["scheduled_at"] <= now:
        return "published"
    return "scheduled"


@router.post("/posts", status_code=201)
def schedule_post(payload: PostCreate, _token=Depends(require_auth)):
    profiles = {p["id"] for p in load_profiles()}
    if payload.profile_id not in profiles:
        raise HTTPException(status_code=404, detail="Profile not found")

    post = create_post(payload.model_dump())
    return {"post": {**post, "status": compute_status(post)}}


@router.get("/posts/{post_id}")
def get_post_status(post_id: str, _token=Depends(require_auth)):
    post = get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return {"post": {**post, "status": compute_status(post)}}