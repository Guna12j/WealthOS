from fastapi import FastAPI

app = FastAPI(
    title="WealthOS API",
    description="Backend API for WealthOS.",
    version="0.1.0",
)

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}