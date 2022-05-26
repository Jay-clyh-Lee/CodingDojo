from flask import render_template, request, session, redirect, flash
from flask_app.models import user, test
from flask_app import app

conditions = ["hopelessness", "negative_thoughts", "cognitive_problems", "focus_problems", "restlessness", "poor_appetite", "worthlessness", "fatigue", "sleep_problems", "loss_of_interest" ]

# test page
@app.route('/tests/new')
def new():
    user_data = {
        "id": session["user_id"]
    }
    return render_template("new.html", logged_in_user = user.User.get_by_id(user_data))

# acquire form data
@app.route('/tests/create', methods=['POST'])
def create():
    data = {}
    for condition in conditions:
        data[condition] = request.form[condition]
    data["user_id"] = session["user_id"]
    # convert string value to int
    for key in data:
        data[key] = int(data[key])

    # calculate severity (add scores)
    test_result = sum(int(x) for x in data.values())
    data["result"] = test_result

    # display level of severity based on test score
    if test_result < 10:
        level = "mild"
    elif test_result >= 10 and test_result < 20:
        level = "moderate"
    else:
        level = "severe"
    session["level"] = level

    print("##############   TEST ON DATA   #############", data)

    # validation not needed. restricted form data input
    # if not test.Test.validate_test(data):
    #     return redirect('/tests/new')
    # create
    test_id = test.Test.create_test(data)
    # return redirect(f'/tests/results/{test_id}')
    return redirect('/dashboard')


@app.route('/tests/show/<int:test_id>')
def show(test_id):
    user_data = {
        "id": session["user_id"]
    }
    data = {                                                           
        "id": test_id,
    }
    return render_template("show.html", logged_in_user = user.User.get_by_id(user_data), test = test.Test.get_by_test_id(data), level = session["level"])

# admin only (do not use for now)
@app.route('/tests/edit/<int:test_id>')
def edit(test_id):
    user_data = {
        "id": session["user_id"]
    }
    data = {                                                           
        "id": test_id,
    }
    return render_template("edit.html", logged_in_user = user.User.get_by_id(user_data), test = test.Test.get_by_test_id(data))

# admin only (do not use for now)
@app.route('/tests/update/<int:test_id>', methods=['POST'])
def update(test_id):
    data = {
        "id": test_id,
        "location" : request.form['location'],
        "description" : request.form['description'],
        "date_sighted": request.form["date_sighted"],
        "count": request.form["count"],
        "user_id": session['user_id']
    }
    if not test.Test.validate_test(data):
        return redirect(f'/tests/edit/{test_id}')
    test.Test.update_test(data)
    return redirect('/dashboard')

# admin only (do not use for now)
@app.route('/tests/delete/<int:test_id>')
def destroy(test_id):
    data = {                                                           
        "id": test_id
    }
    test.Test.destroy_test(data)
    return redirect('/dashboard')
