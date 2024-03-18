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
    

##Product
class BaseProduct(BaseModel):
    pass 
class ProductForCreate(BaseProduct):
    name:String
    description:String
    image:String
    suppiler:String
    price:Float

class ProductForQuery(BaseProduct):
    id:int
    name:String
    description:String
    image:String
    suppiler:String
    price:Float
##Order
class BaseOrder(BaseModel):
    pass
class OrderForCreate(BaseOrder):
    startDate:Date
    endDate:Date
    shipToAddress: String
    status:int
    totalPrice:float
class OrderForQuery(BaseOrder):
    id:int
    startDate:Date
    endDate:Date
    shipToAddress: String
    status:int
    totalPrice:float
    
##Notification

class BaseNotification(BaseModel):
    pass 
class NotificationForCreate(BaseNotification):
    createOn:Date
    cotent:String
class NotificationForQuery(BaseNotification):
    id:int
    createOn:Date
    cotent:String