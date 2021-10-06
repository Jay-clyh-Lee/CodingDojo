from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = 'guess a number or die in this squid game'

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randint(1,100)
    return render_template('index.html', color='red')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)