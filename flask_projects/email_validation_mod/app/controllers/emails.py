from flask import render_template,redirect,request
from werkzeug.utils import validate_arguments
from app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create/email', methods=['POST'])
def create():
    if validate_arguments