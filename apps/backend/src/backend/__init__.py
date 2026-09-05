from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session
from backend.api.router import router

from backend.database.dependencies import get_db

app = FastAPI(
    title="WealthOS API",
    description="Backend API for WealthOS.",
    version="0.1.0",
)

app.include_router(router, prefix="/api")

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/health/database")
def database_health_check(db: Session = Depends(get_db)) -> dict[str, str]:
    db.execute(text("SELECT 1"))
    return {"status": "ok"}