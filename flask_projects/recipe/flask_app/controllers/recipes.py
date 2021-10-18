from flask import render_template, request, session, redirect, flash
from flask_app.models import user, recipe
from flask_app import app

@app.route("/recipes/new")
def index():
    return render_template("new_recipe.html")

@app.route("/recipes/new/create", methods=["POST"])
def create_new():
    data = {
        "title": request.form['title'],
        "details": request.form['details']
    }
    recipe.Recipe.create_recipe(data)
    return redirect("/dashboard")

@app.route("/recipes/view/<int:id>")
def view_recipe(id):
    return render_template("show_recipe.html", recipe = recipe.Recipe.get_by_id(id))

@app.route("/recipes/edit/<int:id>")
def view_recipe(id):
    return render_template("edit_recipe.html", recipe = recipe.Recipe.get_by_id(id))

@app.route("/recipes/delete/<int:id>", methods=["POST"])
def view_recipe(id):
    data = {
        "id": request.form['recipes.id']
    }
    recipe.Recipe.destroy(data)
    return redirect("/dashboard")

