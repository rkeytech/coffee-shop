from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('dashboard.html', title='Dashboard')


@app.route('/stuff')
def stuff():
    stuff = [["Timos", "Zach", "Waiter"],
             ["Giorgos", "Zach", "Waiter"],
             ["Eva", "Zach", "Waiter"]]
    return render_template('stuff.html', stuff=stuff)


@app.route('/products')
def products():
    return render_template('products.html', title='Products')


@app.route('/orders')
def orders():
    orders = [["1", "frappe", "3.40", "Timos", "01/02/2020"],
              ["2", "tost", "1.30", "Eva", "01/03/2020"],
              ["3", "freddo", "4.10", "Timos", "01/01/2020"]]
    return render_template('orders.html', orders=orders)
