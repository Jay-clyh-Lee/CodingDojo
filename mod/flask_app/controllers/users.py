from flask import render_template, request, session, redirect, flash, jsonify
from flask_app.models import user, band
from flask_app import app
from flask_bcrypt import Bcrypt
import requests, os

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_user')
def get_user():
    gamer_tag = request.form['gamer_tag']
    if " " in gamer_tag:
        gamer_tag = gamer_tag.replace(" ", "%20")
    system_type = request.form['system']
    url = f"/{system_type}/{gamer_tag}"
    headers = {"TRN-Api-Key": os.environ.get("API_KEY")}
    response = requests.get(url, headers=headers)

    session["gamer_info"] = response.json()["data"]
    session["kda_ratio"] = response.json()["data"]["kda"]
    # user_data = {
    #     "id" : session["id"]
    #     "gamer_info" : response.json()["data"]
    #     "kda_ratio" : response.json()["data"]["kda"]
    # }
    return redirect('/')
    #return render_template('dashboard.html', logged_in_user = this_user)

@app.route('/register',methods=['POST'])
def register():
    # print(request.form)
    if not user.User.validate_registration(request.form):
        return redirect('/')
    # because of hashed password, we can't pass on the data directly from request.form to our database
    pw_hash = bcrypt.generate_password_hash(request.form['password'])  
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    this_user = user.User.save(data)
    session['user_id'] = this_user
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    if not user.User.validate_login(request.form):
        return redirect('/')
    user_data = {
        'email':request.form['email']
    } 
    user_with_email = user.User.get_by_email(user_data)
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
    return render_template("dashboard.html", logged_in_user = user.User.get_by_id(data), all_bands = band.Band.get_all())