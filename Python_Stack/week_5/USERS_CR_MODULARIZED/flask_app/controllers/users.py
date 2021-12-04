from flask import render_template, request, session, redirect
from flask_app.models import user
from flask_app import app


@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def read():
    users = user.User.get_all()
    return render_template('index.html', users=users)

@app.route('/users/new')
def new_user():
    return render_template('new.html')

@app.route('/add', methods=["POST"])
def create():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    user_id = user.User.save(data)
    return redirect('/users/{{user_id}}/show')

@app.route('/users/<int:id>/show')
def show(id):
    data = {
        "id": id
    }
    this_user = user.User.get_by_id(data)
    return render_template('show.html', user=this_user)

@app.route('/users/<int:id>/edit')
def edit(id):
    data = {
        "id": id
    }
    this_user = user.User.get_by_id(data)
    return render_template('edit.html', user=this_user)

@app.route('/users/<int:id>/update', methods=["POST"])
def update(id):
    user_data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    user.User.update(user_data)
    return redirect('/users')

@app.route('/users/<int:id>/delete')
def destroy(id):
    data = {
        "id": id
    }
    user.User.destory(data)
    return redirect('/users')