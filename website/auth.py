from flask import Blueprint, render_template, url_for, request
import flask
from werkzeug.utils import redirect
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)



# Login 
@auth.route('/login', methods=['GET', 'POST'])
def login():
    """ Login User """
    # data = request.form
    # print(data)
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
    
        user =  User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flask.flash("Logged in successfully!", category='success')
                login_user(user, remember=True)
                return redirect('/')

            else:
                flask.flash("Incorrect password, try again.", category='error')

        else:
            flask.flash("Email doesn\'t exist.", category="error")

    # session.clear()



    return render_template('login.html', user=current_user)


@auth.route("/logout")  
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    logout_user()

    
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """ Register User """

    if request.method == 'POST':
        email = request.form['email']
        firstname = request.form['firstname']
        surname = request.form['surname']
        password1 = request.form['password1']
        password2 = request.form['password2']

        user =  User.query.filter_by(email=email).first()
        if user:
            flask.flash("Email already exist.", category='error')
            return redirect(url_for('auth.register'))

        #check for input errors
        elif len(email) < 3:
            flask.flash('Email error', 'error')
        
        elif firstname or surname < 2:
            flask.flash('Name should be more than 3 charachers', 'error')

        elif password1 != password2:
            flask.flash('Passwords don\'t match ', 'error')

        elif password1 < 6:
            flask.flash('Password must be more than 6 charachers', 'error')


        
        new_user = User(email=email, firstname=firstname, surname=surname, password=generate_password_hash(password1, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        # flash('Account Created!', 'success')
        return redirect(url_for('auth.login'))
        
      

    return render_template('register.html', user=current_user)
