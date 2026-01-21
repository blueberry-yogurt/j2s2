from fastapi import APIRouter
from app.services.quote_service import get_random_quote, scrape_quotes

router = APIRouter(tags=["quotes"])


@router.get("/random-quote")
async def random_quote():
    return await get_random_quote()


@router.post("/scrape")
async def scrape():
    await scrape_quotes()
    return {"message": "명언 스크래핑 완료!"}
