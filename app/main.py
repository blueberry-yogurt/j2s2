from fastapi import FastAPI
from app.core.config import settings
from app.api.routers.health import router as health_router
app = FastAPI(
    title="J2S2 Diary API",
    version="0.1.0",
)
app.include_router(health_router, prefix=settings.API_V1_PREFIX)


@app.get("/")
def root():
    return {"message": "J2S2"}
