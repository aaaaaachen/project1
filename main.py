import flask
from flask import Flask,render_template,request,redirect,make_response
from orm import model
from orm import ormmanage as manage
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    user = request.cookies.get("name")
    return render_template('new_file.html',userinfo = user)


@app.route('/regist',methods=["GET","POST"])
def regist():
    if request.method == "GET":
        print("gettttttttttttttttttttttt")
        return render_template('regist.html')
    elif request.method == "POST":
        print("postpppppppppppppppppppppppppppp")
        username = request.form['username']
        password = request.form['password']

        try:
            manage.insertUser(username,password)
            return redirect('/login')
        except Exception as e:
            print(e)
            redirect('/regist')

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "GET":

        return render_template('login.html')

    elif request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        print(username,password)

        try:
            result = str(manage.checkUser(username,password))
            print(result,type(result))
            res = make_response(redirect('/shoppinglist'))
            res.set_cookie('name',result,expires=datetime.datetime.now()+datetime.timedelta(days=5))
            return res
        except:
            print("errrrorr")
            return redirect('/login')

@app.route('/quit')
def quit():
    res = make_response(redirect('/'))
    res.delete_cookie('name')
    return res


@app.route('/shoppinglist',methods=["GET","POST"])
def shoppinglist():
    user = request.cookies.get("name")
    # username = request.form['username']
    # print(username)
    goods = manage.checkGoods()
    # for good in goods:
        # print(good)

    return render_template('shoppinglist.html',shoppinglist=goods,userinfo=user)

@app.route('/details/<int:num>')
def detail(num):

    infos = manage.checkdetails(num)
    print(infos,type(infos))
    return render_template('details.html',num=num,info = infos)

@app.route('/order/<int:id>',methods=["GET","POST"])
def order(id):
    if request.method == "GET":
        goods = manage.checkGoods()
        for good in goods:
            if good[0] == id:
                goodprice = good[2]
        print(goodprice,"wwwwwwwwwwww")
        return render_template('order.html',id=id,price=goodprice)
    elif request.method == "POST":
        user = request.cookies.get("name")
        num = request.form['num']
        goodprice = request.form['price']
        sum = int(num)*int(goodprice)
        print(user,num,sum)
        manage.addorder(user,id,num,sum)
        return redirect('/shoppinglist')


@app.route('/delgood/<int:id>',methods=["GET","POST"])
def delgood(id):
    if request.method == "GET":
        print("ggggggggggggggggg")
        return render_template('shoppinglist.html',id=id)
    elif request.method == "POST":
        print("pppppppppppppp")
        goods = manage.checkGoods()
        for good in goods:
            print(good.id)
        print(id,type(id))
        delg = manage.del_Good(id)
        print(delg)
        return redirect('/shoppinglist')

@app.route('/addgood',methods=["GET","POST"])
def addgood():
    if request.method == "GET":
        print("gggggggggggtttttttttttttt")
        return render_template('addgood.html')
    elif request.method == "POST":
        print("pppppppppppppoooooooosssssssss")
        goodname = request.form['goodname']
        goodprice = request.form['goodprice']
        result = manage.addGood(goodname,goodprice)
        print(result)
        return redirect('/shoppinglist')

@app.route('/updgood/<int:id>',methods=["GET","POST"])
def updgood(id):
    if request.method == "GET":
        print("getget")
        return render_template('updgood.html',id=id)
    elif request.method == "POST":
        print("postpost")
        goodname = request.form["goodname"]
        goodprice = request.form['goodprice']
        print(goodname,goodprice,id)
        manage.updgood(id,goodname,goodprice)
        return redirect('/shoppinglist')


@app.route('/addinfo/<int:id>',methods=["GET","POST"])
def addinfo(id):
    if request.method == "GET":
        return render_template('addinfo.html',id=id)
    elif request.method == "POST":
        print("pppppppppsssssssstt")
        info = request.form['info']
        manage.addinfo(id,info)
        print(info)

        return  redirect('/shoppinglist')



if __name__ == "__main__":
    app.run()
