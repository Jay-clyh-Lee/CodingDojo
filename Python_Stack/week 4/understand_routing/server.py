from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello():
    msg = "hello world!"
    print(msg)
    return msg

@app.route('/dojo')
def dojo():
    msg = "dojo!"
    print(msg)
    return msg

@app.route('/say/<string:name>')
def say(name):
    msg = f"Hi {name}"
    print(msg)
    return msg

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    msg = f"{word} " * num
    print(msg)
    return msg

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)