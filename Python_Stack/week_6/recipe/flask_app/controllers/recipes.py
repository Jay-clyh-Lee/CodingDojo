from flask_app import render_template, request, session, redirect, flash
from flask_app.models import user, recipe
from flask_app import app

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    recipe_data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instruction" : request.form['instruction'],
        "duration" : request.form['duration'],
        "date_made": request.form["date_made"],
        "user_id": session['user_id']
    }
    if not recipe.Recipe.validate_recipe(recipe_data):
        return redirect('/recipes/new')
    recipe.Recipe.create_recipe(recipe_data)
    return redirect('/user/account')

@app.route('/recipes/new')
def new_recipe():
    user_data = {
        "id": session["user_id"]
    }
    return render_template("new.html", logged_in_user = user.User.get_by_id(user_data))

@app.route('/recipes/<int:recipe_id>/show')
def show_recipe(recipe_id):
    user_data = {
        "id": session["user_id"]
    }
    data = {                                                           
        "id": recipe_id,
    }
    like_data = {
        "user_id": session["user_id"],
        "recipe_id": session["recipe_id"]
    }

    return render_template("show.html", logged_in_user = user.User.get_by_id(user_data), recipe = recipe.Recipe.get_all_by_id(data))
    # return redirect('/recipes/{recipe_id}/edit)

@app.route('/recipes/<int:recipe_id>/edit')
def edit_recipe(recipe_id):
    user_data = {
        "id": session["user_id"]
    }
    data = {                                                           
        "id": recipe_id,
    }
    return render_template("edit.html", logged_in_user = user.User.get_by_id(user_data), recipe = recipe.Recipe.get_all_by_id(data))
    # return redirect('/recipes/{recipe_id}/edit)

@app.route('/recipes/<int:recipe_id>/update', methods=['POST'])
def update_recipe(recipe_id):
    data = {
        "id": recipe_id,
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instruction" : request.form['instruction'],
        "date_made": request.form["date_made"],
        # "user_id": session['user_id']
    }
    if not recipe.Recipe.validate_recipe(data):
        return redirect('dashboard')
    recipe.Recipe.update_recipe(data)
    return redirect('/dashboard')
    # return redirect('/recipes/{recipe_id}/edit)

@app.route('/recipes/<int:recipe_id>/delete')
def destroy_recipe(recipe_id):
    data = {                                                           
        # "user_id": session['user_id'],
        "id": recipe_id
    }
    recipe.Recipe.destroy_recipe(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:recipe_id>/like', methods=['POST'])
def like_recipe(recipe_id):
    like_data = {  
        "user_id": session['user_id'],
        "recipe_id": recipe_id
    }
    recipe.Recipe.like_recipe(like_data)
    return redirect('/recipes/{recipe.id}/show')

@app.route('/recipes/<int:recipe_id>/dislike', methods=['POST'])
def dislike_recipe(recipe_id):
    like_data = {  
        "user_id": session['user_id'],
        "recipe_id": recipe_id
    }
    recipe.Recipe.dislike_recipe(like_data)
    return redirect('/dashboard')