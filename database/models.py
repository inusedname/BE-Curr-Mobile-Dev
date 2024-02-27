
from database import database
from sqlalchemy import Column, Integer, String, Float


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
    
#Luong hoat dong: lay tat ca productId dua vao OrderDetail, Tao 1 mao key la productId, value la so luong cua no
#Tao 1 list de chua Product cung voi amount cua chung
#Dua vao OrderDetail de lay ra gia tri
class Order(database.Base):
    __tablename__ = "Order"
    id = Column(Integer, primary_key=True, index=True)
    orderStatus=Column(Integer) # 0 la chua giao 1 la dang giao 2 la da giao thanh cong
    description=Column(Integer)
class OrderDetail(database.Base):
    __tablename__ = "OrderDetail"
    id = Column(Integer, primary_key=True, index=True)
    orderId=Column(Integer)  #chung 1 orderId 
    productId=Column(Integer)
    quantity=Column(Integer,default=0.0)
class Product(database.Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, index=True)    
    image=Column(String)
    name=Column(String)
    amount=Column(Float,default=0.0)
    # orderDetailId=Column(Integer)
    