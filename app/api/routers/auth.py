from fastapi import APIRouter, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordRequestForm

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
"""

@router.post("/auth/login", response_model=TokenResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> TokenResponse:
    user = await User.get_or_none(username=form_data.username)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    print("ff")
    token = create_access_token(subject=user.username)

    return TokenResponse(access_token=token)