from flask import render_template,request,session,redirect,flash
from flask_app.models import book
from flask_app import app

@app.route("/")
def index():
    redirect('/authors')

@app.route("/books", methods=['POST'])
def create_books():
    book.Book.save(request.form)
    return redirect("/books")

@app.route("/books/<int:id>")
def show_book():
    data = {
        'id': request.form['id']
    }
    return render_template("book.html", book = book.Book.get_one(data))

