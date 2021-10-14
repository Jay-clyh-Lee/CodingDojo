from flask import render_template,request,session,redirect,flash
from flask_app.models import author,book
from flask_app import app

@app.route("/")
def index():
    return redirect('/authors')

@app.route("/authors")
def authors():
    return render_template("authors.html", authors = author.Author.get_all())

@app.route("/create/author", methods=['POST'])
def create_author():
    print("Pay MEGA ATTENTION HERE. WHY U NO UNDERSTAND THSI STILL")
    print(request.form) #attn
    author.Author.save(request.form)
    return redirect("/authors")

@app.route("/authors/<int:id>")
def show_author(id): #attn
    data = {
        'id': id
    }
    return render_template("show_author.html", author = author.Author.get_by_id(data), favorited_books = book.Book.