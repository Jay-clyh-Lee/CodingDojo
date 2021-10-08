from flask import Flask, render_template, request, session, redirect
from user import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users/new')
def new():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def create():
    print(request.form)
    data = request.form
    User.save(data)
    return redirect('/users')

@app.route('/users')
def show_users():
    all_users = User.get_all()
    #print(all_users)
    return render_template('users.html', users = all_users)

if __name__ == "__main__":
    app.run(debug=True)