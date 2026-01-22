import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.api.routers.health import router as health_router
from app.api.routers.users import router as users_router
from app.api.routers.auth import router as auth_router
from app.api.routers.me import router as me_router
from app.api.routers.diary import router as diary_router
from app.api.routers.quote import router as quote_router
from app.api.routers.bookmark import router as bookmark_router
from app.api.routers.question import router as question_router
from app.api.routers.diary_bookmark import router as diary_bookmark_router

from app.core.config import settings
from app.db.database import init_db, close_db


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        version="0.1.0",
    )

    BASE_DIR = Path(__file__).resolve().parent  # app/
    templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

    app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

    #페이지 라우트
    @app.get("/login", include_in_schema=False)
    async def login_page(request: Request):
        return templates.TemplateResponse("login.html", {"request": request})

    @app.get("/signup", include_in_schema=False)
    async def signup_page(request: Request):
        return templates.TemplateResponse("userAdd.html", {"request": request})

    # 라우터 등록 (공통 prefix: /api/v1)
    api_prefix = settings.API_V1_PREFIX
    app.include_router(health_router, prefix=api_prefix)
    app.include_router(users_router, prefix=api_prefix)
    app.include_router(auth_router, prefix=api_prefix)
    app.include_router(me_router, prefix=api_prefix)
    app.include_router(diary_router, prefix=api_prefix)
    app.include_router(bookmark_router, prefix=api_prefix)
    app.include_router(question_router, prefix=api_prefix)
    app.include_router(diary_bookmark_router, prefix=api_prefix)
    app.include_router(quote_router, prefix=api_prefix)

    @app.on_event("startup")
    async def on_startup() -> None:
        # 1. DB 초기화 (반드시 최상단에 위치)
        await init_db()

        # 2. 명언 스크래핑 실행
        # 로컬에서 이미 import 되어 있는지 확인 (상단에 from app.services.scraper import scrape_quotes 필요)
        from app.services.scraper import scrape_quotes

        print("🚀 서버 시작: 명언 데이터 동기화 작업을 시작합니다.")
        try:
            await scrape_quotes()
            print("✅ 서버 시작: 명언 데이터 동기화 완료!")
        except Exception as e:
            # 스크래핑 에러가 나더라도 서버 자체가 죽지 않도록 예외 처리
            print(f"❌ 서버 시작 중 스크래핑 실패: {e}")

    @app.on_event("shutdown")
    async def on_shutdown() -> None:
        await close_db()

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

