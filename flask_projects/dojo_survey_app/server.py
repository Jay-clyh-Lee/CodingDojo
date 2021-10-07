from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process')
def process():
    session['Name'] = request.form(['name'])
    session['Dojo Location'] = request.form(['loc'])
    session['Favorite Language'] = request.form(['lang'])
    session['Comment'] = request.form(['comment'])
    return redirect('/')

@app.route('/result')
def result():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)

