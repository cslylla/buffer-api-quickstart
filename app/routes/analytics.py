import hashlib
from fastapi import APIRouter, Depends, HTTPException
from app.auth import require_auth
from app.store import get_post

router = APIRouter(tags=["analytics"])


def fake_metrics(post_id: str) -> dict:
    # deterministic numbers per post_id
    h = hashlib.sha256(post_id.encode()).hexdigest()
    n1 = int(h[:4], 16)
    n2 = int(h[4:8], 16)
    n3 = int(h[8:12], 16)

    impressions = 500 + (n1 % 5000)
    clicks = 5 + (n2 % 300)
    likes = 1 + (n3 % 800)

    return {
        "impressions": impressions,
        "clicks": clicks,
        "likes": likes,
        "engagement_rate": round((clicks + likes) / max(impressions, 1), 4),
    }


@router.get("/analytics/{post_id}")
def get_analytics(post_id: str, _token=Depends(require_auth)):
    post = get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return {
        "post_id": post_id,
        "metrics": fake_metrics(post_id),
    }