from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
            pass
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
            pass
        elif len(lastName) < 2:
            flash('Last name must be greater than 1 character.', category='error')
            pass
        elif password != confirmPassword:
            flash('Passwords do not match.', category='error')
            pass
        elif len(password) < 7:
            flash('Password must be greater than 6 characters.', category='error')
            pass
        else:
            flash('Account created!', category='success')
            #add user to database

    return render_template("sign_up.html")