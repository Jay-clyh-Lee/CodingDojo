from flask import render_template, redirect, session, request
from models import user, post
from __init__ import app
from config.mysqlconnection import connectToMySQL

@app.route('/posts/create', methods=['POST'])
def create():
    data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "price": request.form["price"],
        "quantity": request.form["quantity"],
        "user_id": session['user_id']
    }
    if not post.Post.validate_post(data):
        return redirect('/posts/new')
    post.Post.create_post(data)
    return redirect('/dashboard')

@app.route('/posts/new')
def new():
    user_data = {
        "id": session["user_id"]
    }
    return render_template("new.html", logged_in_user = user.User.get_by_id(user_data))

@app.route('/posts/show/<int:post_id>')
def show(post_id):
    user_data = {
        "id": session["user_id"]
    }
    data = {                                                           
        "id": post_id,
    }
    return render_template("show.html", logged_in_user = user.User.get_by_id(user_data), post = post.post.get_by_id(data))

@app.route('/posts/edit/<int:post_id>')
def edit(post_id):
    user_data = {
        "id": session["user_id"]
    }
    data = {                                                           
        "id": post_id,
    }
    return render_template("edit.html", logged_in_user = user.User.get_by_id(user_data), post = post.post.get_by_id(data))

@app.route('/posts/update/<int:post_id>', methods=['POST'])
def update(post_id):
    data = {
        "id": post_id,
        "name" : request.form['name'],
        "description" : request.form['description'],
        "price": request.form["price"],
        "quantity": request.form["quantity"],
        "user_id": session['user_id']
    }
    if not post.Post.validate_post(data):
        return redirect(f'/posts/edit/{post_id}')
    post.Post.update_post(data)
    return redirect('/dashboard')

@app.route('/posts/delete/<int:post_id>')
def destroy(post_id):
    data = {                                                           
        "id": post_id
    }
    post.Post.destroy_post(data)
    return redirect('/dashboard')

@app.route('/posts/<int:post_id>/like', methods=['POST'])
def buy_post(post_id):
    buyer_data = {  
        "user_id": session['user_id'],
        "post_id": post_id
    }
    query = f"UPDATE posts SET sold=sold+1 WHERE id = {post_id};"
    connectToMySQL(db).query_db(query)
    post.Post.buy_post(buyer_data)
    return redirect(f'/posts/show/{post_id}')