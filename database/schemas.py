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
    
##Order
class BaseOrder(BaseModel):
   pass

class OrderForCreate(BaseOrder):
    orderStatus:int
    description:String
    totalPrice:float
    
class OrderForQuery(BaseOrder):
    id:int
    orderStatus:int
    description:String
    totalPrice:float   
      
##OrderDetail
class BaseOrderDetail(BaseModel):
    pass

class OrderDetailForCreate(BaseOrderDetail):
    orderId:int
    productId:int
    dateStart:String
    dateEnd : String
    quantity:Integer
    
class OrderDetailForQuery(BaseOrderDetail):
    id:int
    orderId:int
    productId:int
    dateStart:String
    dateEnd : String
    quantity:Integer
    
##Product
class BaseProduct(BaseModel):
    pass

class ProductForCreate(BaseProduct):
    image:String
    name:String
    amount:float
    
class ProductForQuery(BaseProduct):
    id : int 
    image:String
    name:String
    amount:float 