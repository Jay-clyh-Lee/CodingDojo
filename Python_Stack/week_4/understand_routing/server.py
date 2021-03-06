from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello():
    msg = "hello world!"
    return msg

@app.route('/dojo')
def dojo():
    msg = "dojo!"
    return msg

@app.route('/say/<string:name>')
def say(name):
    msg = f"Hi {name}"
    return msg

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    msg = f"{word} " * num
    return msg

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)