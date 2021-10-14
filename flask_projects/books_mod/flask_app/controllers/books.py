from flask import render_template,request,session,redirect,flash
from flask_app.models import author,book
from flask_app import app

@app.route("/books")
def books():
    return render_template("books.html", books = book.Book.get_all())

@app.route("/create/book", methods=['POST'])
def create_book():
    print("Pay MEGA ATTENTION HERE. WHY U NO UNDERSTAND THSI STILL")
    print(request.form) #attn
    data = {
        "title":request.form['title'],
        "pages": request.form['pages']
    }
    book.Book.save(data)
    return redirect("/books")

@app.route("/books/<int:id>")
def show_book(id): #attn
    data = {
        'id':id
    }
    return render_template("show_book.html", book = book.Book.get_by_id(data), unfavored_authors = author.Author.unfavorited_authors(data))

@app.route('/join/author',methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    author.Author.add_favorite(data)
    return redirect(f"/book/{request.form['book_id']}")