from flask import render_template,url_for,redirect,flash, request
from flask_login import login_user, logout_user, login_required,current_user
from . import auth
from ..models import  User
from .form import  RegistrationForm, LoginForm
from .. import db


@auth.route('/login',methods=["GET","POST"])
def login():
    
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_hash(login_form.password.data):
            flash('Invalid username or Password')
        login_user(user,login_form.remember.data)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('main.index'))
    title = "blog login"
       
    return render_template('auth/login.html', login_form=login_form ,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@auth.route('/register', methods=["GET","POST"])
def signUp():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data,pass_s=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/sign.html',form=form) 





