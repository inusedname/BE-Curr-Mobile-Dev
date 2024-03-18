
from database import database
from sqlalchemy import Column, Integer, String, Float,ForeignKey,Date
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates
arbitrary_types_allowed = True
import datetime
class User(database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, unique=True, index=True)
    pw = Column(String)

class Transaction(database.Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    senderId = Column(Integer)
    receiverId = Column(Integer)
    amount = Column(Float, default=0.0)
    


#---------------------------------------------------------------------#

from enum import Enum

class OrderStatus(Enum):
    shipping = 0
    delivered = 1
    paid:2
from abc import ABC #lop truu tuong
class Product(database.Base):
    __tablename__ = "product"
    id = Column(Integer,primary_key=True,index=True)
    name=Column(String)
    description=Column(String)
    image=Column(String)
    suppiler=Column(String) 
    price=Column(Float,default=0.0) 
class Order(database.Base):
    __tablename__ = "order"
    id = Column(Integer,primary_key=True,index=True)
    startDate= Column(Date)
    endDate=Column(Date)
    shipToAddress = Column(String)
    status=Column(Integer)
    totalPrice=Column(Float,default=0.0)
    @validates('status')
    def validate_status(self, key, value):
        if not isinstance(value, OrderStatus):
            raise ValueError("Status must be an instance of OrderStatus Enum")
        return value.value
    def __init__(self, startDate, endDate, shipToAddress, status, totalPrice):
        self.startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d').date()
        self.endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d').date()
        self.shipToAddress = shipToAddress
        self.status = status
        self.totalPrice = totalPrice
class Notification(database.Base):
    __tablename__ = "notification"
    id = Column(Integer,primary_key=True,index=True)
    createOn=Column(Date)
    cotent=Column(String)
    

    