import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routers.health import router as health_router
from app.api.routers.users import router as users_router
from app.api.routers.auth import router as auth_router
from app.api.routers.me import router as me_router
from app.api.routers.diary import router as diary_router # <- 2026.01.21 심상보 추가
from app.api.routers.quote import router as quote_router
from app.api.routers.bookmark import router as bookmark_router  # <- 2026.01.21 심상보 추가
from app.api.routers.question import router as question_router # <- 2026.01.21 심상보 추가
from app.api.routers.diary_bookmark import router as diary_bookmark

from app.core.config import settings
from app.db.database import init_db, close_db



def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        version="0.1.0",
    )

    #  라우터 등록 (공통 prefix: /api/v1)
    api_prefix = settings.API_V1_PREFIX
    app.include_router(health_router, prefix=api_prefix)
    app.include_router(users_router, prefix=api_prefix)  # POST /users (회원가입)
    app.include_router(auth_router, prefix=api_prefix)   # POST /auth/login (로그인)
    app.include_router(me_router, prefix=api_prefix)     # GET /me (JWT 보호)
    app.include_router(diary_router, prefix=api_prefix)  # <- 2026.01.21 심상보 추가
    app.include_router(bookmark_router, prefix=api_prefix)  # <- 2026.01.21 심상보 추가
    app.include_router(question_router, prefix=api_prefix) # <- 2026.01.21 심상보 추가
    app.include_router(diary_bookmark, prefix=api_prefix)

    app.include_router(quote_router, prefix=api_prefix)

    app.include_router(quote_router, prefix=api_prefix)

    app.include_router(saying_router, prefix=api_prefix)

    app.include_router(quote_router, prefix=api_prefix)

    app.mount("/static", StaticFiles(directory="static"), name="static")

    # startup / shutdown
    @app.on_event("startup")
    async def on_startup() -> None:
        await init_db()

    @app.on_event("shutdown")
    async def on_shutdown() -> None:
        await close_db()

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)