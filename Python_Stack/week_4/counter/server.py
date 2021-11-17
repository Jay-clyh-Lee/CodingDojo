from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "counter the times your mom has been ravaged by huge cocks. It's infinitely uncountable."

@app.route('/')
def index():
    if "counter" not in session:
        session["counter"] = 0
    if "visits" not in session:
        session["visits"] = 0
    session["counter"] += 1
    session["visits"] += 1
    return render_template('index.html', counter = session["counter"], visits = session["visits"])

@app.route('/add')
def add1():
    if "counter" not in session:
        return redirect('/')
    session["counter"] += 1
    return render_template('index.html', counter = session["counter"], visits = session["visits"])

@app.route('/add_multiple', methods = ['POST'])
def add_multiple():
    if "counter" not in session:
        return redirect('/')
    print(f'the request form is: {request.form}')
    print(f'the request.form.to_dict() is: {request.form.to_dict()}')
    session["counter"] += int(request.form["custom_number"])
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('index.html',counter = session["counter"], visits = session["visits"])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return render_template('index.html', counter = 0, visits = 0)


if __name__ == "__main__":
    app.run(debug=True)