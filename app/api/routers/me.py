from fastapi import APIRouter, Depends
from app.core.deps import get_current_user
from app.models.user import User
from app.schemas.user import UserOut

router = APIRouter(tags=["me"])


@router.get("/me", response_model=UserOut)
async def me(user: User = Depends(get_current_user)) -> UserOut:
    return UserOut(username=user.username, password=user.password_hash)
