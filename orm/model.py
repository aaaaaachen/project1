class Goods():
    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price
    def __str__(self):
        return "id:%s   name:%s   price:%s",(self.id,self.name,self.price)


from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/flaskdb",
                                    encoding='utf8', echo=True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)

from sqlalchemy import *

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(20), nullable=False)
    password = Column(String(50), nullable=False)

class Goods(Base):
    __tablename__ = 'goods'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    goodname = Column(String(20), nullable=False)
    goodprice = Column(Integer, nullable=False)


class Goodinfo(Base):
    __tablename__ = "goodinfo"
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    goodid = Column(Integer,ForeignKey(Goods.id,ondelete="cascade",onupdate="cascade"),nullable=False)
    info = Column(String(50),default=".....",nullable=False)

class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    userid = Column(Integer,ForeignKey(User.id,ondelete='cascade',onupdate='cascade'),nullable=False)
    goodid = Column(Integer,ForeignKey(Goods.id,ondelete="cascade",onupdate="cascade"),nullable=False)
    goodnum = Column(Integer,nullable=False)
    sum = Column(Integer,nullable=False)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)