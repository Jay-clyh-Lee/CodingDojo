from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", x=8, y=8, color1='red', color2='black')

@app.route('/<int:x>')
def index_row(x):
    return render_template("index.html", x=x, y=8, color1='red', color2='black')

@app.route('/<int:x>/<int:y>')
def index_col(x, y):
    return render_template("index.html", x=x, y=y, color1='red', color2='black')

@app.route('/<int:x>/<int:y>/<string:color1>')
def index_color1(x, y, color1):
    return render_template("index.html", x=x, y=y, color1=color1, color2='black')

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def index_color2(x, y, color1, color2):
    return render_template("index.html", x=x, y=y, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)
