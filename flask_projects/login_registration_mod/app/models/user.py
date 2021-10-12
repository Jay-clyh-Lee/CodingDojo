from ..config.mysqlconnection import connectToMySQL
from flask import flash
import re	

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+[a-zA-Z]$')

class User:
    db = "login_registration_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query) 
        users = []
        for u in results:
            users.append(cls(u))
        return users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data) 
        return cls(results[0])
    
    @classmethod
    def get_last_one(cls):
        query = "SELECT * FROM users WHERE ORDER BY id DESC LIMIT 1;"
        results = connectToMySQL(cls.db).query_db(query) 
        return cls(results[0])

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET (first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, password=%(password)s, updated_at=NOW());"
        return connectToMySQL(cls.db).query_db(query,data)


    @staticmethod
    def validate_registration(data):
        is_valid = True
        # for names
        if not data.match(data['first_name']):
            flash("Enter a valid first name.", "error")
            is_valid=False
        if not data.match(data['last_name']):
            flash("Enter a valid last name.", "error")
            is_valid=False
        # for email
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email!", "error")
            is_valid=False
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query, data) # reminder: results is returned as a list of dictionaries.
        if len(results) >= 1:
            flash("Email already taken.", "error")
            is_valid=False
        # for passwords
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters long", "error")
            is_valid=False
        if data['password'] != data['confirm_password']:
            flash("Passwords don't match.", "error")
            is_valid=False
        return is_valid
    
    @staticmethod
    def valid_login(data):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query, data)
        if len(results) == 0:
            flash("Email does not exist.")
            is_valid=False
        # if not EMAIL_REGEX.match(email['email']):
        #     flash("Invalid Email!!!")
        #     is_valid=False
        query2 = "SELECT * FROM users WHERE password = %(password)s;"
        es
        return is_valid