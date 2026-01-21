from fastapi import APIRouter, HTTPException, status

from app.schemas.user import UserCreate, UserOut
from app.models.user import User
from app.core.security import hash_password

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def signup(payload: UserCreate) -> UserOut:
    exists = await User.filter(email=payload.email).exists()
    if exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists",
        )

    user = await User.create(
        email=payload.email,
        password_hash=hash_password(payload.password),
    )
    return UserOut(id=user.id, email=user.email)
