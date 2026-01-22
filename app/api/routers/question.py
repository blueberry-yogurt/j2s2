from fastapi import APIRouter, Depends, HTTPException
from app.repositories.question_repo import QuestionRepository
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/question", tags=["question"])


@router.get("/random")
async def get_random_reflection_question(
    current_user: User = Depends(get_current_user),
):
    """
    자아성찰을 위한 랜덤 질문을 하나 반환합니다.
    """
    question = await QuestionRepository.get_random_question()

    if not question:
        raise HTTPException(status_code=404, detail="등록된 질문이 없습니다.")
    return {"id": question.id, "question_text": question.question_text}
