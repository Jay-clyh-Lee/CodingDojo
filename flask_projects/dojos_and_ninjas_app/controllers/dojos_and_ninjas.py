from flask import render_template, request, redirect

from dojos_and_ninjas_app import app
from dojos_and_ninjas_app.models.dojo import Dojo
from dojos_and_ninjas_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def users():
    return render_template("dojos.html", dojos=Dojo.get_all())

@app.route('/dojos/create',methods=['POST'])
def create():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojo')

@app.route('/dojos/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user=Dojo.get_one(data))

@app.route('/dojos/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show_user.html",user=Dojo.get_one(data))

@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):\
    data ={
        'id': id
    }
    Dojo.destroy(data)
    return redirect('/users')
