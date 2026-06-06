from fastapi import FastAPI

from backend.app.core.config import settings

app = FastAPI(title="LEVIT v2 Backend", version="0.1.0")


@app.get("/health", tags=["system"])
def health() -> dict[str, str | int]:
    return {
        "status": "ok",
        "environment": settings.levit_env,
        "port": settings.levit_api_port,
    }
