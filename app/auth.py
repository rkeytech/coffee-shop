from flask import Blueprint, render_template, redirect, flash, request
from .models import User

# Create the blueprint
auth = Blueprint('auth', __name__)


# Routes
@auth.route('/login')
def login():
    return "<p>Login Page</p>"


@auth.route('/logout')
def logout():
    return "<p>Logout Page</p>"


@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up Page</p>"
