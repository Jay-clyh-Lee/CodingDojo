from flask import render_template, redirect, session, request
from models import user, post
from __init__ import app
from config.mysqlconnection import connectToMySQL

@app.route('/posts/create', methods=['POST'])
def create():
    data = {
        "comment": request.form['comment'],
        "user_id": session['user_id']
    }
    if not post.Post.validate_post(data):
        return redirect('/dashboard')
    post.Post.save(data)
    return redirect('/dashboard')

# @app.route('/posts/new')
# def new():
#     user_data = {
#         "id": session["user_id"]
#     }
#     return render_template("new.html", logged_in_user = user.User.get_by_id(user_data))

@app.route('/posts/showUser/<int:poster_id>')
def show(poster_id):
    user_data = {
        "id": session["user_id"]
    }
    poster_data = {                                                           
        "id": poster_id,
    }
    return render_template("show.html", logged_in_user = user.User.get_by_id(user_data), post_user = user.User.get_by_id_with_posts(poster_data))

@app.route('/posts/edit/<int:post_id>')
def edit(post_id):
    user_data = {
        "id": session["user_id"]
    }
    post_data = {                                                           
        "id": post_id,
    }
    return render_template("edit.html", logged_in_user = user.User.get_by_id(user_data), post = post.Post.get_by_id(post_data))

@app.route('/posts/update/<int:post_id>', methods=['POST'])
def update(post_id):
    data = {
        "id": post_id,
        "comment" : request.form['comment'],
        "user_id": session['user_id']
    }
    if not post.Post.validate_post(data):
        return redirect(f'/posts/edit/{post_id}')
    post.Post.update(data)
    return redirect('/dashboard')

@app.route('/posts/delete/<int:post_id>')
def destroy(post_id):
    data = {                                                           
        "id": post_id
    }
    post.Post.delete(data)
    return redirect('/dashboard')

@app.route('/posts/like/<int:post_id>', methods=['POST'])
def like_post(post_id):
    liker_data = {  
        "user_id": session['user_id'],
        "post_id": post_id
    }
    post.Post.like_post(liker_data)
    return redirect('/dashboard')