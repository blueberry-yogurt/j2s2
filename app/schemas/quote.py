from pydantic import BaseModel, EmailStr, Field

class QuoteOut(BaseModel):
    title: str = Field(..., description="제목")
    content: str