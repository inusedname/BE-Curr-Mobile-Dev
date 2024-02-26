from pydantic import BaseModel
from sqlalchemy import *
from database.database import Base

## User
class BaseUser(BaseModel):
    pass

class UserForCreate(BaseUser):
    phone: str
    pw: str

class UserForQuery(BaseUser):
    id: int
    phone: str

    
## Transaction
class BaseTransaction(BaseModel):
    pass

class TransactionForCreate(BaseTransaction):
    senderId: int
    receiverId: int
    amount: float

class TransactionForQuery(BaseTransaction):
    id: int
    senderId: int
    receiverId: int
    amount: float