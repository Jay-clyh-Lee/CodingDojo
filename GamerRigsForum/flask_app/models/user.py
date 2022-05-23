from config.mysqlconnection import connectToMySQL
from flask import flash
import re	
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    
    db = "gamer_rigs_forum"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.liked_posts = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users LEFT JOIN posts ON posts.user_id = id;"
        results = connectToMySQL(cls.db).query_db(query) 
        users = []
        for u in results:
            users.append(cls(u))
        return users

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) == 0:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) == 0:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id_with_posts(cls,data):
        query = "SELECT * FROM users LEFT JOIN posts ON users.id = posts.user_id WHERE posts.user_id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        this_user = []
        print("RESULTS", results)
        for row in results:
            # user_data = { 
            #     'id': row['users.id'],
            #     'first_name': row['first_name'],
            #     'last_name': row['last_name'],
            #     'email': row['email'],  
            #     'password': row['password'],
            #     'created_at': row['users.created_at'],
            #     'updated_at': row['users.updated_at'],
            # }

            print("###################################", row)
            this_user.append(cls(row))
        return this_user
        # if len(results) == 0:
        #     return False
        # print(cls(results[0]))
        # return cls(results[0])

    @classmethod
    def get_posts_by_user_id(cls,data):
        query = "SELECT * FROM users JOIN likes ON likes.user_id = users.id JOIN posts ON likes.post_id = posts.id WHERE users.id = %(user_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        for row in results:
            this_user = cls(row)
            post_data = {
                "id": row["posts.id"],
                'comment': row['comment'],
                'user_id': row['user_id'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            }
            this_user.liked_posts.append(post_data)
        if len(results) == 0:
            return False
        return cls(results[0])

    @staticmethod
    def validate_registration(data):
        is_valid = True
        # for names
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters.", "register")
            is_valid=False
        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters", "register")
            is_valid=False
        # for email
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email!", "register")
            is_valid=False
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query, data)
        if len(results) >= 1:
            flash("Email already taken.", "register")
            is_valid=False
        # for passwords
        if len(data['password']) < 6:
            flash("Password must be at least 8 characters long", "register")
            is_valid=False
        if data['password'] != data['confirm_password']:
            flash("Passwords don't match.", "register")
            is_valid=False
        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query, data)
        if len(results) == 0:
            flash("Email does not exist.", "login")
            is_valid=False
        if len(data['email']) == 0:
            flash("Email field cannot be empty", "login")
            is_valid=False
        if len(data['password']) == 0:
            flash("Password field cannot be empty", "login")
            is_valid=False
        return is_valid