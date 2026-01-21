from fastapi import APIRouter, HTTPException, status, Request
from fastapi.templating import Jinja2Templates

from app.schemas.user import UserCreate, UserOut
from app.models.user import User
from app.core.security import hash_password

templates = Jinja2Templates(directory="templates")

router = APIRouter(prefix="/users", tags=["users"])
"""
@router.get("")
async def root(request: Request):
    return templates.TemplateResponse("userAdd.html", {"request": request})
"""

@router.post("", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def signup(payload: UserCreate) -> UserOut:
    exists = await User.filter(username=payload.username).exists()
    if exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="name already exists",
        )
    user = await User.create(
        username=payload.username,
        password_hash=hash_password(payload.password),
        email=payload.email,
    )
    return UserOut(username=user.username, password=user.password_hash, email=user.email)
