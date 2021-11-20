from flask import Flask, redirect, render_template, session, request
import random
import datetime

app = Flask(__name__)
app.secret_key = "gold mines"

@app.route("/")
def index():
    if "gold" not in session:
        session["gold"] = 0
    gold = session["gold"]
    if "color" not in session:
        session["color"] = "black"
    color = session["color"]
    if "random_gain" not in session:
        session["random_gain"] = 0
    random_gain = session["random_gain"]
    if "datetime" not in session:
        session["datetime"] = None
    datetime = session["datetime"]
    if "building" not in session:
        session["building"] = "nowhere"
    building = session["building"]
    return render_template('index.html', gold = gold, color = color, gain = random_gain, datetime = datetime, building = building) 

@app.route("/process_money", methods = ["POST"])
def process_money():
    bld = request.form['building']
    session["building"] = bld
    if bld == "farm":
        randnum = random.randint(-20, 21)
    elif bld == "cave":
        randnum = random.randint(-5, 11)
    elif bld == "house":
        randnum = random.randint(-2, 6)
    elif bld == "casino":
        randnum = random.randint(-50, 51)
    else:
        pass

    if randnum > 0:
        session["color"] = "green"
    else: 
        session["color"] = "red"

    amount = int(session["gold"])
    amount += randnum
    session["random_gain"] = randnum
    session["gold"] = amount
    session["datetime"] = str(datetime.datetime.now())[:19]
    return redirect('/')

@app.route('/quit')
def quit_game():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)