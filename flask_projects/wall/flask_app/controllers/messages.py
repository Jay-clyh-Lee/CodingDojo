from flask import render_template, request, session, redirect, flash
from flask_app.models import user, message, comment
from flask_app import app

@app.route('/messages/create', methods=['POST'])
def create_message():
    data = {
        "content": request.form['content'],
        "user_id": session['user_id']
    }
    if not message.Message.validate_message(data):
        return redirect('dashboard')
    message.Message.create_message(data)
    return redirect('/dashboard')

@app.route('/messages/<int:message_id>/like', methods=['POST'])
def like_message(message_id):
    liker_data = {  
        "user_id": session['user_id'],
        "message_id": message_id
    }
    message.Message.like_message(liker_data)
    return redirect('/dashboard')

@app.route('/messages/<int:message_id>/dislike', methods=['POST'])
def like_message(message_id):
    liker_data = {  
        "user_id": session['user_id'],
        "message_id": message_id
    }
    message.Message.dislike_message(liker_data)
    return redirect('/dashboard')

@app.route('/messages/<int:message_id>/edit')
def edit_message(message_id):
    data = {                                                           
        "id": message_id,
    }
    return render_template("edit_message.html", message=message.Message. get_message_by_id(data))
    # return redirect('/messages/{message_id}/edit)

@app.route('/messages/<int:message_id>/update', methods=['POST'])
def update_message(message_id):
    data = {                                                           
        "id": message_id,
        "content": request.form["content"]
    }
    message.Message.update_message(data)
    return redirect('/dashboard')
    # return redirect('/messages/{message_id}/edit)

@app.route('/messages/<int:message_id>/destroy')
def destroy_message(message_id):
    data = {                                                           
        # "user_id": session['user_id'],
        "id": message_id
    }
    message.Message.destroy_message(data)
    return redirect('/dashboard')