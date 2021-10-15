from flask import render_template, request, session, redirect, flash
from flask_app.models import user, message, comment
from flask_app import app

@app.route('/messages/create', methods=['POST'])
def create_message():
    data = {
        "content": request.form['content'],
        "user_id": session['user_id']
    }
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

@app.route('/messages/<int:message_id>/destroy', methods=['POST'])
def destroy_message(message_id):
    data = {                                                                    
        "user_id": session['user_id'],
        "message_id": message_id
    }
    message.Message.destroy_message(data)
    return redirect('/dashboard')