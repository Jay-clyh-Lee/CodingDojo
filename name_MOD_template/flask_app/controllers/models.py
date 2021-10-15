from flask import render_template, request, session, redirect, flash
from flask_app.models.user import User
from flask_app import app
from flask_bcrypt import Bcrypt    

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def process():
    if not Email.is_valid(request.form):
        return redirect('/')
    Email.save(request.form)
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