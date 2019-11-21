from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Student(Base):
   __tablename__ = "Product"
   id = Column(Integer, primary_key=True)
   Name = Column(String)
   Price = Column(Float)
   Picture_Link = Column(String)
   Description = Column(String)
