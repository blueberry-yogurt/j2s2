from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
import random
from app.models.quote import Quote
from app.schemas.quote import QuoteOut

router = APIRouter(prefix="/quote", tags=["Quote"])

# db 총 숫자 가져와서 랜덤 id 값으로 제목과 내용 출력
@router.get("/",response_model=QuoteOut)
async def quote():
    total = await Quote.all().count()
    random_number = random.randint(0, total)
    quote_title = await Quote.get_or_none(id = random_number)

    return {
        "title": quote_title.title,
        "content": quote_title.content
    }