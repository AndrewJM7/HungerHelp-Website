import bcrypt
from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from models import User
from users.forms import RegisterForm, LoginForm
from flask_login import login_user
from datetime import datetime


users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            flash('Email address already exists')
            return render_template('users/register.html', form=form)

        # create a new user with the form data
        new_user = User(email=form.email.data,
                        firstname=form.firstname.data,
                        lastname=form.lastname.data,
                        phone=form.phone.data,
                        password=form.password.data,
                        role='user')

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('users.login'))

    return render_template('users/register.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # check if user exists, password is correct and one-time password is correct
        if not user or not bcrypt.checkpw(form.password.data.encode('utf-8'), user.password):
            flash('Please check your login details and try again')
            return render_template('users/login.html', form=form)
        # if user exists and passwords are correct, logs in user
        login_user(user)
        # update last login and current login time
        user.last_login = user.current_login
        user.current_login = datetime.now()
        db.session.add(user)
        db.session.commit()
    return render_template('users/login.html', form=form)

