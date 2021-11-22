from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key="meow"


@app.route('/')
def index():
    if "tries" not in session:
        session["tries"] = 0
    if "my_number" not in session:
        session["my_number"] = random.randint(1, 101)
        # print(f'THE TYPE OF THIS SESSION IS :: : : : : : {type(session["my_number"])}')
    return render_template('index.html', my_number = session["my_number"], tries = session["tries"])

@app.route('/guess', methods=['POST'])
def guess():
    session["user_number"] = int(request.form['guess'])
    session["tries"] += 1
    # print(f'OMWQEWLKJS:LFJLFJGGJ ++++++++++++++++++++++++++++++ {type(request.form["guess"])}')
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)