from datetime import datetime
from typing import Literal

from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    full_name: str = Field(...,min_length=3, max_length=150)
    email: EmailStr
    role: Literal["administrador", "gestor", "consultor"] = "consultor"
    is_active: bool = True
    
class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128)
    
class UserUpdate(BaseModel):
    full_name: str | None = Field(default=None, min_length=3, max_length=150)
    role: Literal["administrador", "gestor", "consultor"] | None = None
    is_active: bool | None = None


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }