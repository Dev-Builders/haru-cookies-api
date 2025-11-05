from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from app.models.client import ClientSource


class ClientCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    adress: str
    source: ClientSource


class ClientResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    adress: str
    source: ClientSource
    created_at: datetime

    class Config:
        from_attributes = True


class ClientUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    adress: Optional[str] = None
    source: Optional[ClientSource] = None