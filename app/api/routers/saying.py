from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
import random
from app.models.saying import Saying
from app.schemas.saying import SayingOut

router = APIRouter(prefix="/saying", tags=["Saying"])

# db 총 숫자 가져와서 랜덤 id 값으로 제목과 내용 출력
@router.get("/",response_model=SayingOut)
async def saying():
    total = await Saying.all().count()
    random_number = random.randint(0, total)
    saying_title = await Saying.get_or_none(id = random_number)

    return {
        "title": saying_title.title,
        "content": saying_title.content
    }