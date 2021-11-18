from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key="meow"

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    number = request.form



if __name__ == "__main__":
    app.run(debug=True)