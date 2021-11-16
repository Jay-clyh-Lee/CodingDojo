from flask import Flask, render_template, redirect

app = Flask(__name__)
@app.route('/')
def index():
    return redirect('/play')

@app.route('/play')
def play():
    return render_template('play.html', times = 3, color = 'lightblue')

@app.route('/play/<int:x>')
def costom_times(x):
    return render_template('play.html', times = x, color = 'lightblue')

@app.route('/play/<int:x>/<string:color>')
def custom_color(x, color):
    return render_template('play.html', times = x, color = color)


if __name__ == "__main__":
    app.run(debug=True)