from flask import render_template, request, session, redirect, flash
from flask_app.models import user, sasquatch
from flask_app import app

@app.route('/sasquatches/create', methods=['POST'])
def create():
    data = {
        "location" : request.form['location'],
        "description" : request.form['description'],
        "date_sighted": request.form["date_sighted"],
        "count": request.form["count"],
        "user_id": session['user_id']
    }
    if not sasquatch.Sasquatch.validate_sasquatch(data):
        return redirect('/sasquatches/new')
    sasquatch.Sasquatch.create_sasquatch(data)
    return redirect('/dashboard')

@app.route('/sasquatches/new')
def new():
    user_data = {
        "id": session["user_id"]
    }
    return render_template("new.html", logged_in_user = user.User.get_by_id(user_data))

@app.route('/sasquatches/show/<int:sasquatch_id>')
def show(sasquatch_id):
    user_data = {
        "id": session["user_id"]
    }
    data = {                                                           
        "id": sasquatch_id,
    }
    return render_template("show.html", logged_in_user = user.User.get_by_id(user_data), sasquatch = sasquatch.Sasquatch.get_by_id(data))

@app.route('/sasquatches/edit/<int:sasquatch_id>')
def edit(sasquatch_id):
    user_data = {
        "id": session["user_id"]
    }
    data = {                                                           
        "id": sasquatch_id,
    }
    return render_template("edit.html", logged_in_user = user.User.get_by_id(user_data), sasquatch = sasquatch.Sasquatch.get_by_id(data))

@app.route('/sasquatches/update/<int:sasquatch_id>', methods=['POST'])
def update(sasquatch_id):
    data = {
        "id": sasquatch_id,
        "location" : request.form['location'],
        "description" : request.form['description'],
        "date_sighted": request.form["date_sighted"],
        "count": request.form["count"],
        "user_id": session['user_id']
    }
    if not sasquatch.Sasquatch.validate_sasquatch(data):
        return redirect(f'/sasquatches/edit/{sasquatch_id}')
    sasquatch.Sasquatch.update_sasquatch(data)
    return redirect('/dashboard')

@app.route('/sasquatches/delete/<int:sasquatch_id>')
def destroy(sasquatch_id):
    data = {                                                           
        "id": sasquatch_id
    }
    sasquatch.Sasquatch.destroy_sasquatch(data)
    return redirect('/dashboard')
