from flask import render_template,request,session,redirect
from app.models.survey import Survey
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create/survey', methods=['POST'])
def create():
    if Survey.validate_survey(request.form):
        Survey.save(request.form)
        return redirect('/result')
    return redirect('/')

@app.route('/result')
def show_result():
    return render_template('result.html', survey = Survey.get_last())