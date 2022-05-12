from config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt        
import re

bcrypt = Bcrypt(app) 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User():
  
    db = "gamer_rigs_forum"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE users.id = %(id)s"
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("mydb").query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        # let user update their profile
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s WHERE users.id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE users.id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_user_with_posts(cls, data):
        query = "SELECT * FROM users LEFT JOIN posts ON users.id = post.user_id WHERE users.id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        this_user = []
        for row in results:
            this_user.append(cls(row))
        return this_user

    @classmethod
    def get_user_and_liked_posts(cls, data):
        query = "SELECT * FROM users LEFT JOIN likes ON likes.user_id = users.id LEFT JOIN posts ON likes.post_id = posts.id WHERE users.id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        this_user = []
        for row in results:
            # the owner of this post
            poster_data = {
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "comment": row["comment"],
                "user_id": row["posts.user_id"], # owner of the post that this user liked
            }
            # others who like this post
            liker_data = {
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "user_id": row["liker.user_id"],
                "post_id": row["liker.post_id"],
            }
        

    @staticmethod
    ## add name validation API
    def validate_registration(form_data):
        is_valid = True
        if len(form_data['first_name']) < 1:
            flash("First name cannot be empty.")
            is_valid = False
        if len(form_data['last_name']) < 1:
            flash("Last name cannot be empty.")
            is_valid = False
        if int(form_data['email']) < 200:
            flash("Calories must be 200 or greater.")
            is_valid = False
        if len(form_data['password']) < 6:
            flash("passwords must be at least 6 characters.")
            is_valid = False
        return is_valid