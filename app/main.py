from fastapi import FastAPI
from app.routes import health, oauth, profiles, posts, analytics

app = FastAPI(
    title="Buffer API Quickstart (Mock)",
    version="0.1.0",
    description="A lightweight mock Buffer-style API for developer onboarding demos.",
)

app.include_router(health.router)
app.include_router(oauth.router)
app.include_router(profiles.router)
app.include_router(posts.router)
app.include_router(analytics.router)