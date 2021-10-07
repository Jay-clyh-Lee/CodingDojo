from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'counter_app m'

@app.route('/')
def index():
    if "counter" not in session:
        session["counter"] = 0
    else:
        session["counter"] += 1
    return render_template("index.html")

@app.route('/add2')
def add2():
    if "counter" not in session:
        session["counter"] = 0
    else:
        session["counter"] += 2
    return render_template("index.html")

@app.route('/custom_number', methods=['POST'])
def customer_number(number):
    session['counter'] += number
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
