from fastapi import APIRouter, HTTPException, status, Request
from fastapi.templating import Jinja2Templates

from app.models.user import User
from app.schemas.auth import LoginRequest, TokenResponse
from app.core.security import verify_password, hash_password
from app.core.jwt import create_access_token

templates = Jinja2Templates(directory="templates")
router = APIRouter(tags=["auth"])
"""
@router.get("")
async def root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
"""

@router.post("/auth/login", response_model=TokenResponse)
async def login(payload: LoginRequest) -> TokenResponse:
    user = await User.get_or_none(username=payload.username)
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    token = create_access_token(subject=user.username)

    return TokenResponse(access_token=token)
