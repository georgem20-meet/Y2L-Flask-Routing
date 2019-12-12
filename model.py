from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Product(Base):
   __tablename__ = "Product"
   id = Column(Integer, primary_key=True)
   Name = Column(String)
   Price = Column(Float)
   Picture_Link = Column(String)
   Description = Column(String)
   def __repr__(self):
   	return self.Name + "\n" + self.Price + "\n" + self.Description
class Cart(Base):
   __tablename__ = "Cart"
   id = Column(Integer, primary_key=True)
   productID = Column(String)

