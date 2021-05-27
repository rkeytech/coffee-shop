from flask import Flask, render_template, redirect, flash, request
from database import db
from models import User
from forms import UserForm

# App Initialization
# Create a Flask Instance
app = Flask(__name__)

# Create a secret for form validation
app.config['SECRET_KEY'] = 'not so much secure key'

# Create a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initiliaze the database
db.init_app(app)


# ROUTING
@app.route('/')
def dashboard():
    return render_template('dashboard.html', title='Dashboard')


# STUFF
@app.route('/stuff')
def stuff():
    stuff = User.query.all()
    context = {
        'stuff': stuff
    }
    return render_template('stuff.html', context=context, title='Stuff')


@app.route('/stuff/add', methods=['POST', 'GET'])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        try:
            # Create the user and add it to the database
            user = User(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                job=form.job.data,
                wage=form.wage.data
            )
            db.session.add(user)
            db.session.commit()
            # Create message for the success
            flash(
                f'Stuff {form.first_name.data} added successfully!', 'success'
            )
            # Redirect back to stuff
            return redirect('/stuff')
        except Exception as e:
            flash(
                f'Error with adding {form.first_name.data}!', 'danger'
            )
            return redirect('/stuff')

    # Create the context dictionary to pass to template
    context = {
        'form': form
    }
    return render_template('add_user.html', context=context, title='Add new stuff')


@app.route('/stuff/profile/<int:pk>')
def view_user(pk):
    user = User.query.get_or_404(pk)
    context = {
        'user': user
    }
    return render_template('profile.html', context=context, title='User')


@app.route('/stuff/edit/<int:pk>', methods=['GET', 'POST'])
def edit_user(pk):
    user = User.query.get_or_404(pk)
    form = UserForm(
        first_name=user.first_name, last_name=user.last_name,
        email=user.email, job=user.job, wage=user.wage
    )
    if request.method == 'POST':
        try:
            user.first_name = form.first_name.data
            user.last_name = form.last_name.data
            user.email = form.email.data
            user.job = form.job.data
            user.wage = form.wage.data
            db.session.commit()
            flash(
                f'User {user.first_name} updated successfully!', 'success'
            )
            return redirect('/stuff')
        except:
            flash(
                f'There was a problem with updating user {user.first_name}!', 'danger'
            )
            return redirect('/stuff')
    context = {
        'form': form,
        'submit': ('Update stuff', 'warning')
    }
    return render_template('add_user.html', context=context, title='Update user...')


# PRODUCTS
@ app.route('/products')
def products():
    return render_template('products.html', title='Products')


# ORDERS
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
