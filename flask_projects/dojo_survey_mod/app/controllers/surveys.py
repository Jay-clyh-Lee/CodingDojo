from flask import render_template,request,session,redirect
from app.models.survey import Survey
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    if not Survey.validate_survey(request.form):
        return redirect('/')
    Survey.save(request.form)
    return redirect('/')

@app.route('/result')
def show_result():
    return render_template('result.html', surveys = Survey.get_all())