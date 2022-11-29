from pydantic import BaseModel, EmailStr
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: str

class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    name: str
    last_name: str
    password: str


class User(UserBase):
    id: int
    name: str
    last_name: str

    class Config:
        orm_mode = True


class StockMarket(BaseModel):
    id: int
    symbol: str
    open_price: Optional[str] = "0.0"
    higher_price: Optional[str] = "0.0"
    lower_price: Optional[str] = "0.0"
    variation_price: Optional[str] = "0.0"
