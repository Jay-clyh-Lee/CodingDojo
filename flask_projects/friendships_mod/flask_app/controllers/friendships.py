from flask import render_template, request, session, redirect
from flask_app.models import friendship
from flask_app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/friendships',methods=['POST'])
def add_friendship():
    Friend.save(request.form)
    return redirect('/results')

@app.route('/results')
def results():
    return render_template("results.html",emails=Email.get_all())

@app.route('/destroy/<int:id>')
def destroy_email(id):
    data = {
        "id": id
    }
    Email.destroy(data)
    return redirect('/results')