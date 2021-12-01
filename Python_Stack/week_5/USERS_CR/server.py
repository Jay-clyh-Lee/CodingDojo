from flask import Flask, render_template, redirect, request, session 
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "secrets"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def read():
    query = "SELECT * FROM users;"
    results = connectToMySQL('users_schema').query_db(query)
    users = []
    for user in results:
        users.append(user)
    return render_template('read.html', users=users)

@app.route('/users/new')
def new_user():
    return redirect('/')

@app.route('/add', methods=["POST"])
def create():
    query = "INSERT INTO users (first_name, last_name, email, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW());"
    new_user_id = connectToMySQL('users_schema').query_db(query)
    return redirect('/users')



if __name__=="__main__":
    app.run(debug=True)