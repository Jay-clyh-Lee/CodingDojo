from flask import render_template, request, session, redirect
from app.models.user import User
from app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register',methods=['POST'])
def register():
    if not User.validate_registration(request.form):
        return redirect('/')
    User.save(request.form)
    return redirect('/dashboard')

@app.route('/login')
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    return redirect('/dashboard')

    

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", user = User.get_all())

@app.route('/destroy/<int:id>')
def destroy_email(id):
    data = {
        "id": id
    }
    Email.destroy(data)
    return redirect('/results')