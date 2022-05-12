from flask import render_template, redirect, request, session, flash
from application import app
from models.user import User
from flask_bcrypt import Bcrypt    


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        	"first_name": request.form['first_name'],
        	"last_name": request.form['last_name'],
        	"email": request.form['email'],
        	"password": pw_hash
            }
    User.save(data)
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    data = {
        "email": request.form["email"]
        }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")