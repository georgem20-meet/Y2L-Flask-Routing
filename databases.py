from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(Name, Price, Picture_Link, Description):
    Product_object = Student(
        Name = Name,
        Price = Price,
        Picture_Link = Picture_Link,
        Description = Description)
    session.add(Product_object)
    session.commit()


