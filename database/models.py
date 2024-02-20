from pydantic import BaseModel
from sqlalchemy import *
from database.database import Base


class User(BaseModel):
    name: str
    phone: str
    pw: str
    balance: float = 0.0


class Transaction(BaseModel):
    senderId: int
    receiverId: int
    amount: float
