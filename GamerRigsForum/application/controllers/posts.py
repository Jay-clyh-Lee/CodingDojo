from flask import render_template, redirect, session, request
from application import app
from application.models.post import Post
from application.models.user import User
from flask import render_template, request, session, redirect, flash
from models import user, post
from __init__ import app
from config.mysqlconnection import connectToMySQL

db = "gamer_rigs_forum"

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

@app.route('/posts/<int:post_id>/buy', methods=['POST'])
def buy_post(post_id):
    buyer_data = {  
        "user_id": session['user_id'],
        "post_id": post_id
    }
    query = f"UPDATE posts SET quantity=quantity-1, sold=sold+1 WHERE id = {post_id};"
    connectToMySQL(db).query_db(query)
    post.Post.buy_post(buyer_data)
    return redirect(f'/posts/show/{post_id}')

############################

@app.route('/new/post')
def new_post():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    return render_template('new_post.html',user=User.get_user(data))

@app.route('/create/post',methods=['POST'])
def create_post():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Post.validate_post(request.form):
        return redirect('/new/post')
    data = {
        "name": request.form["comment"],
        "user_id": session["user_id"]
        }
    Post.save(data)
    return redirect('/dashboard')

@app.route('/edit/post/<int:id>')
def edit_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit.html", edit=Post.get_one(data), user=User.get_by_id(user_data))

@app.route('/update/post',methods=['POST'])
def update_post():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Post.validate_post(request.form):
        return redirect('/new/post')
    data = {
        "comment": request.form["name"],
        "id": request.form['id']
    }
    Post.update(data)
    return redirect('/dashboard')

@app.route('/view/post/<int:id>')
def show_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show.html", post = Post.get_one(data), user = User.get_by_id(user_data))

@app.route('/destroy/post/<int:id>')
def destroy_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Post.delete(data)
    return redirect('/dashboard')