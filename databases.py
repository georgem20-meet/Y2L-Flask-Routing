from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(Name, Price, Picture_Link, Description):
    Product_object = Product(
        Name = Name,
        Price = Price,
        Picture_Link = Picture_Link,
        Description = Description)
    session.add(Product_object)
    session.commit()

def edit_product(Name, Price, Picture_Link, Description):
   Product_object = session.query(
       Product).filter_by(
       Name=Name).first()
   Product_object.Price = Price
   Product_object.Picture_Link = Picture_Link
   Product_object.Description = Description
   session.add(Product_object)
   session.commit()

def delete_product(Name):
      session.query(Product).filter_by(
       Name = Name).delete()
      session.commit()

def query_all():
   Product_object = session.query(
      Product_object).all()
   return Product_object

def query_by_name(Name):
   Product_object = session.query(
       Product_object).filter_by(
       Name = Name).first()
   return Product_object

def Add_To_Cart(productID):
	Add_To_Cart = Cart(
		productID = productID)
	session.add(Add_To_Cart)
	session.commit