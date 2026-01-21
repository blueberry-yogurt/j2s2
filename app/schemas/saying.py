from pydantic import BaseModel, EmailStr, Field

class SayingOut(BaseModel):
    title = str
    content: str