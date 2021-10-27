from flask import render_template, request, redirect, session
from ..models import event

@app.route('/')
def index():
    return render_template('index.html')


