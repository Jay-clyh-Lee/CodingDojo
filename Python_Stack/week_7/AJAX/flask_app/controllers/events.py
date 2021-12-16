from flask import render_template, request, redirect, session
from ..models import event, user
from flask_app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    form_data = {
        "id": session["user_id"]
    }
    user = user.User.get_user(form_data)
    return render_template('dashboard.html', user=user)