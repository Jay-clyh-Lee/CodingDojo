from flask import render_template, request, session, redirect
from ..models import user
from flask_app import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def read():
    return render_template('read.html', users=user.User.get_all())

@app.route('/users/new')
def new_user():
    return redirect('/')

@app.route('/add', methods=["POST"])
def create():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["first_name"]
    }
    user.User.save(data)
    return redirect('/users')

