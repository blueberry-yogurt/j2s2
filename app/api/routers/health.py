from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["health"],
)


@router.get(
    "",
    summary="Health Check",
    description="서버 및 애플리케이션 상태 확인용 엔드포인트",
)
async def health_check():
    return {"status": "ok"}
