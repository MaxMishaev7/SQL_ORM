import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
  __tablename__ = 'publisher'
  id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
  name = sq.Column(sq.String(length=40), nullable=False)

  def __str__(self):
    return f'Publisher {self.id}: {self.name}'
  
  
class Book(Base):
  __tablename__ = 'book'
  id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
  title = sq.Column(sq.String(length=120), nullable=False)
  id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)

  publisher = relationship(Publisher, backref='book')

  def __str__(self):
    return f'Book {self.id}: {self.title}\n\tpublisher: {self.id_publisher}'
  
 
class Shop(Base):
  __tablename__ = 'shop'
  id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
  name = sq.Column(sq.String(length=40), nullable=False)

  def __str__(self):
    return f'Shop {self.id}: {self.name}'


class Stock(Base):
  __tablename__ = 'stock'
  id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
  id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False) 
  id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
  count = sq.Column(sq.Integer, nullable=True)

  book = relationship(Book, backref='stock')
  shop = relationship(Shop, backref='stock')

  def __str__(self):
    return f'Stock {self.id}:\n\tid_book: {self.id_book}\n\tid_shop: {self.id_shop}\n\tcount: {self.count}'
  

class Sale(Base):
  __tablename__ = 'sale'
  id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
  price = sq.Column(sq.REAL, nullable=True) 
  date_sale = sq.Column(sq.Date, nullable=False)
  id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
  count = sq.Column(sq.Integer, nullable=False)

  stock = relationship(Stock, backref='sale')

  def __str__(self):
    return f'Sale {self.id}:\n\tprice={self.price}\n\tdate_sale={self.date_sale}\n\tid_stock={self.id_stock}\n\tcount={self.count}'

def create_tables(engine):
  Base.metadata.drop_all(engine)
  Base.metadata.create_all(engine)  