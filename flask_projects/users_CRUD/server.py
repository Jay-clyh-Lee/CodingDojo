from flask import Flask, render_template, request, session, redirect
from users import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def show_users():
    return render_template('users.html', users = User.get_all())

@app.route('/users/new')
def new():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def create():
    print(request.form)
    data = request.form
    User.save(data)
    return redirect('/users')

@app.route('/users/show/<int:id>')
def show_user(id):
    data = {
        "id":id
    }
    return render_template("show_user.html", user = User.get(data))

@app.route('/users/edit/<int:id>')
def edit_user(id):
    data = {
        "id":id
    }
    return render_template("edit_user.html", user = User.get(data))

@app.route('/users/edit/<int:id>', methods=['POST'])
def update_user():
    User.update(request.form)
    # data = {
    #     "id":user_id
    # }
    # User.edit(data)
    return redirect('/users')
    
@app.route('/users/destroy/<int:id>')
def destroy_user(id):
    data = {
        "id":id
    }
    User.destroy(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)