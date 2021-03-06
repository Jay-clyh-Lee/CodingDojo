from flask import render_template, request, session, redirect, flash
from app.models.user import User
from app import app
from flask_bcrypt import Bcrypt    

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register',methods=['POST'])
def register():
    print(request.form)
    if not User.validate_registration(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # because of hashed password, we can't pass on the data directly from request.form to our database
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    session['user_id'] = User.save(data)
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    user_data = {
        'email':request.form['email']
    } 
    user_with_email = User.get_by_email(user_data)
    if not user_with_email:
        flash("incorrect email/password", "login_error")
        return redirect('/')
    if not bcrypt.check_password_hash(user_with_email.password, request.form['password']):
        flash("incorrect email/password", "login_error")
        return redirect('/')
    session['user_id'] = user_with_email.id
    flash("successfully logged in.")
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": session["user_id"]
    }
    return render_template("dashboard.html", user=User.get_by_id(data))
