from fastapi import FastAPI
from app.routes import health

app = FastAPI(
    title="Buffer API Quickstart (Mock)",
    version="0.1.0",
    description="A lightweight mock Buffer-style API for developer onboarding demos.",
)

app.include_router(health.router)