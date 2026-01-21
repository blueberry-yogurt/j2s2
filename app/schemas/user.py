from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    username: str
    password: str = Field(min_length=8, max_length=64)
    email: EmailStr


class UserOut(BaseModel):
    username: str
    password: str #= Field(min_length=8, max_length=64)
    email: EmailStr
    class Config:
        from_attributes = True
