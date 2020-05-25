from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('dashboard.html', title='Dashboard')


@app.route('/stuff')
def stuff():
    return render_template('stuff.html', title='Stuff')


@app.route('/products')
def products():
    return render_template('products.html', title='Products')


@app.route('/orders')
def orders():
    return render_template('orders.html', title='Orders')
