from flask import render_template,request,session,redirect,flash
from flask_app.models import author
from flask_app import app

@app.route("/authors", methods=['POST'])
def create_books():
    author.Author.save(request.form)
    return redirect("/authors/show")

@app.route("/authors/<int:id>")
def show_book():
    data = {
        'id': request.form['id']
    }
    return render_template("show_author.html", book = author.Author.get_one(data))
