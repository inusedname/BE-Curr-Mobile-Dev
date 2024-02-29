
from database import database
from sqlalchemy import Column, Integer, String, Float,ForeignKey
from sqlalchemy.orm import relationship

arbitrary_types_allowed = True

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
    totalPrice=Column(Integer) #gia tien
    order_details = relationship('OrderDetail', back_populates='Order')
    
    
class OrderDetail(database.Base):
    __tablename__ = "OrderDetail"
    id = Column(Integer, primary_key=True, index=True)
    dateStart=Column(String) 
    dateEnd=Column(String)
    quantity=Column(Integer,default=0.0) # so luong
    order = relationship('Order', back_populates='OrderDetail')
    product = relationship('Product', back_populates='OrderDetail')
    orderId=Column(Integer,ForeignKey('Order.id'))  #chung 1 orderId 
    productId=Column(Integer,ForeignKey('Product.id'))
    
    
class Product(database.Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, index=True)    
    image=Column(String)
    name=Column(String)
    amount=Column(Float,default=0.0)  #gia tien
    order_details = relationship('OrderDetail', back_populates='Product')
    