from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html", number=3, color='lightblue')

@app.route('/play/<int:number>')
def display(number):
    return render_template("index.html", number = number, color = "lightblue")

@app.route('/play/<int:number>/<string:color>')
def display_lvl2(number, color = 'lightblue'):
    return render_template("index.html", number = number, color = color)

if __name__=="__main__":
    app.run(debug=True)

