from flask import render_template, request, session, redirect, flash
from flask_app.models import user, recipe
from flask_app import app
from flask_bcrypt import Bcrypt  

bcrypt = Bcrypt(app)

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    if "user_id" not in session:
        return redirect('/index')
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect('/index')
    else:
        data = {
            "title":  request.form['title'],
            "description": request.form['description'],
            "instruction":request.form["instruction"],
            "user_id": session['user_id']
        }
        this_recipe = recipe.Recipe.create_recipe(data) # this gets the id
        return redirect(f'/dashboard/{this_recipe}')
    return redirect('/dashboard')