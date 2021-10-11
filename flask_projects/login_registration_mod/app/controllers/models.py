from flask import render_template, request, session, redirect
from app.models.model_1 import Class_name
from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def process():
    if not Email.is_valid(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/results')

@app.route('/dashboard')
def results():
    return render_template("dashboard.html", user = User.get_all())

@app.route('/destroy/<int:id>')
def destroy_email(id):
    data = {
        "id": id
    }
    Email.destroy(data)
    return redirect('/results')