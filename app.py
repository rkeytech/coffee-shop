from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy import SQLAlchemy
from datetime import datetime


# Create a Flask Instance
app = Flask(__name__)
# Create a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafe.db'
# Create a secret for form validation
app.config['SECRET_KEY'] = 'not so much secure key'


# Basic Routing
@app.route('/')
def dashboard():
    return render_template('dashboard.html', title='Dashboard')


@app.route('/stuff')
def stuff():
    stuff = [[0, "Timos", "Zach", "Waiter"],
             [1, "Giorgos", "Zach", "Waiter"],
             [2, "Eva", "Zach", "Waiter"]]
    return render_template('stuff.html', stuff=stuff, title='Stuff')


@app.route('/profile/<pk>')
def profile(pk):
    context = [0, "Timos", "Zach", "Waiter"]
    return render_template('profile.html', title=context[1], context=context)


@ app.route('/products')
def products():
    return render_template('products.html', title='Products')


@ app.route('/orders')
def orders():
    orders = [["1", "frappe", "3.40", "Timos", "01/02/2020"],
              ["2", "tost", "1.30", "Eva", "01/03/2020"],
              ["3", "freddo", "4.10", "Timos", "01/01/2020"]]
    return render_template('orders.html', orders=orders, title='Orders')


# Custom Error Pages
@ app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='404 Error'), 404


@ app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html', title='500 Error'), 500
