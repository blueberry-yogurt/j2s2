from fastapi import APIRouter, HTTPException
import random
from app.models.quote import Quote
from app.services.scraper import  scrape_quotes
#from app.schemas.quote import QuoteOut

router = APIRouter(prefix="/quote", tags=["Quote"])


# db 총 숫자 가져와서 랜덤 id 값으로 제목과 내용 출력
"""
@router.get("/", response_model=QuoteOut)
async def quote():
    total = await Quote.all().count()
    random_number = random.randint(0, total)
    quote_title = await Quote.get_or_none(id=random_number)

    return {"title": quote_title.title, "content": quote_title.content}
"""

@router.get("/random")
async def get_random_quote():
    await scrape()
    # 1. 전체 개수 파악
    count = await Quote.all().count()
    if count == 0:
        raise HTTPException(status_code=404, detail="저장된 명언이 없습니다. 스크래핑을 먼저 실행하세요.")

    # 2. 랜덤 인덱스 선택 후 하나 가져오기
    #random_index = random.randint(0, count - 1)
    quote = await Quote.all().offset(count-1).first()

    return {
        #"id": quote.id,
        "content": quote.content,
        "author": quote.author
    }

async def scrape():
    value = await scrape_quotes()
