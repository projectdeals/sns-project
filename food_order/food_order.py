import uuid

from flask import Flask, render_template, request, session,redirect,url_for
from mail import send_mail
from common.database import Database
from model.customer import Customer
from model.item import Item
from model.user import User


app = Flask(__name__)
app.secret_key = "nandhu"

food = {"50.0": "Hamburger", "100.0": "Pizza", "30.0": "Ice Cream", "55.0": "Sandwitch", "60.0": "Chocolate Milkshake",
         "175.0": "Mini Combo Fastfood"}
# food = {"50.0": "Pepsi"}
user_email = {}
total=[]
sets = []
uid = [uuid.uuid4().hex]
@app.route('/')
def hello_world():
    return render_template("login.html")


@app.before_first_request
def initiate():
    Database.initialize()



@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/home', methods=['post'])

def login_check():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    if User.validate(email, password):
        User.login(email)
    else:
        return render_template("login.html")
    username = email.split('@')[0]
    user_email[username] =email
    items = Item.get_items()
    return render_template("profile.html", username=username, items=items)


@app.route('/auth/register', methods=['post'])
def register_check():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

    User.register(email, password)
    return render_template("register_auth.html", email=session['email'])


final = 0


@app.route('/order_item', methods=['post'])
def add_item():
    price = request.form['price']
    quantity = request.form['quantity']
    cal = float(price) * int(quantity)
    item = {"item_name": food[price], "price": cal, "quantity": quantity}
    for name,email in zip(user_email.keys(),user_email.values()):
        username = name
        usermail = email
        break
    Customer.add_items(uid,username, item)
    data = Customer.get_item(uid)
    for val in data:
        total.append(val['items'][0]['price'])
    items = Item.get_items()
    for i in total:
        sets.append(int(i))
    con = sum(set(sets))
    total.clear()
    return render_template("profile.html", username=username, items=items,total_price =con)
@app.route('/success',methods=['post'])
def success():
    fo = []
    pi = []
    for name,email in zip(user_email.keys(),user_email.values()):
        username = name
        usermail = email
        break
    data = Customer.get_item(uid)
    for val in data:
        fo.append(val['items'][0]['item_name'])
        pi.append(val['items'][0]['price'])

    t = request.form['total']
    send_mail(usermail,username,fo,pi,t)
    uid.clear()
    sets.clear()
    total.clear()
    uid.append(uuid.uuid4().hex)
    return render_template("success.html")
@app.route('/logout')
def logout():
    User.logout()
    return render_template("login.html")


if __name__ == '__main__':
    app.run()
