from flask import render_template, request, session, redirect, flash
from flask_app.models import user, band
from flask_app import app

@app.route('/bands/new')
def new_band():
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": session["user_id"]
    }
    return render_template("new_band.html", logged_in_user = user.User.get_by_id(data))

@app.route('/mybands')
def my_bands():
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": session["user_id"]
    }
    return render_template("show_bands.html", logged_in_user = user.User.get_by_id(data), all_bands = band.Band.get_all())

@app.route('/bands/create', methods=['POST'])
def create():
    if "user_id" not in session:
        return redirect('/')
    if not band.Band.validate_band(request.form):
        return redirect('/bands/new')
    data = {
        "name":  request.form['name'],
        "genre": request.form['genre'],
        "home_city":request.form["home_city"],
        "user_id": session["user_id"]
    }
    band.Band.create_band(data)
    # this_band = band.Band.create_band(data) # this gets the id
    return redirect('/mybands')
    # return redirect(f'/dashboard/{this_band}')

@app.route('/bands/edit/<int:id>')
def edit_band(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": session["user_id"]
    }
    band_data = {
        "id": id
    }
    return render_template("edit_band.html", logged_in_user = user.User.get_by_id(data), band = band.Band.get_by_id(band_data))

@app.route('/bands/update',methods=['POST'])
def update_band():
    if 'user_id' not in session:
        return redirect('/')
    if not band.Band.validate_band(request.form):
        return redirect('/dashboard')
    data = {
        "name": request.form['name'],
        "genre": request.form['genre'],
        "home_city": request.form['home_city'],
        "id": request.form['id']
    }
    band.Band.update(data)
    return redirect('/dashboard')

@app.route('/bands/delete/<int:id>')
def destroy_band(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": id
    }
    band.Band.destroy(data)
    return redirect('/dashboard')

# @app.route('/mybands/quit/<int:band_id>', methods = ['POST'])
# def quit_bands(band_id):
#     if "user_id" not in session:
#         return redirect('/')
#     data = {
#         "id": band_id
#     }
#     user.User.quit_joined_band(data)
#     return redirect('/mybands')