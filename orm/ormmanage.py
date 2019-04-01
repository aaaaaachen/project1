from orm import model
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/flaskdb",
                                    encoding='utf8', echo=True)
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def insertUser(username,password):
    result = session.add(model.User(username=username,password=password))
    session.commit()
    session.close()
    print("添加成功")
    print(result)
def checkUser(username,password):
    result = session.query(model.User).filter(model.User.username==username).filter(model.User.password==password).first().username
    if result:
        return result
    else:
        return -1
def checkGoods():
    result = session.query(model.Goods.id,model.Goods.goodname,model.Goods.goodprice)
    print(result)
    return result

def addorder(user,id,num,sum):
    userid = session.query(model.User).filter(model.User.username == user).first().id
    result = session.add(model.Orders(userid=userid,goodid=id,goodnum=num,sum=sum))
    print(result)
    session.commit()
    session.close()
    return result


def checkdetails(num):
    try:
        result = session.query(model.Goodinfo.info).filter(model.Goodinfo.goodid == num).first()
        print(result)
    except Exception as e:
        print("checkdetails error")
        print(e)
    finally:
        session.close()
        return result

def del_Good(id):
    try:
        result = session.query(model.Goods).filter(model.Goods.id == id).delete()
    except Exception as e:
        print(e)
    finally:
        session.commit()
        session.close()
        return result

def addGood(goodname,goodprice):
    try:
        result = session.add(model.Goods(goodname=goodname,goodprice=goodprice))
    except Exception as e:
        print(e)
    finally:
        session.commit()
        session.close()
        print("添加成功")
        print(result)

def updgood(id,goodname,goodprice):
    try:
        result = session.query(model.Goods).filter(model.Goods.id == id).first()
        result.goodname = goodname
        result.goodprice = goodprice
    except Exception as e:
        print(e)
    finally:
        session.commit()
        session.close()

def addinfo(id,info):
    print(id,"ssssssssssssss")
    try:

        result = session.add(model.Goodinfo(goodid=id,info=info))
        print("okkk")

    except:
        print(result)
        print("error")
    finally:
        session.commit()
        session.close()

def checkGoodinfo():
    result = session.query(model.Goodinfo.id,model.Goodinfo.info)
    return result
