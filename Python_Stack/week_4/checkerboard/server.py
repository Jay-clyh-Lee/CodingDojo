from flask import Flask, render_template, redirect

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', x=8, y=8, color1='red', color2='black')

@app.route('/<int:x>')
def X(x):
    return render_template('index.html', x=x, y=8, color1='red', color2='black')

@app.route('/<int:x>/<int:y>')
def Y(x,y):
    return render_template('index.html', x=x, y=y, color1='red', color2='black')

@app.route('/<int:x>/<int:y>/<string:color1>')
def color1(x,y,color1):
    return render_template('index.html', x=x, y=y, color1=color1, color2='black')

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def color2(x,y,color1,color2):
    return render_template('index.html', x=x, y=y, color1=color1, color2=color2)

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>/<string:border>')
def border(x,y,color1,color2,border):
    return render_template('index.html', x=x, y=y, color1=color1, color2=color2, border=border)


if __name__ == "__main__":
    app.run(debug=True)