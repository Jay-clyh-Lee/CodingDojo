from ..config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# NAME_REGEX = re.compile(r'^[a-zA-Z]+[a-zA-Z]$')

class User:
    db = "band_together"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f'{self.first_name} + {self.last_name}'
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if len(result) == 0:
            return False
        return cls(result[0])

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        if len(result) == 0:
            return False
        return cls(result[0])

    @staticmethod
    def validate_registration(data):
        is_valid = True
        # for names
        # if not NAME_REGEX.match(data['first_name']):
        #     flash("Enter a valid first name.", "register_error")
        #     is_valid=False
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters long.", "register_error")
            is_valid=False
        # if not NAME_REGEX.match(data['last_name']):
        #     flash("Enter a valid last name.", "register_error")
        #     is_valid=False
        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters long.", "register_error")
            is_valid=False
        # for email
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email!", "registration")
            is_valid=False
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query, data) # reminder: results is returned as a list of dictionaries.
        if len(results) >= 1:
            flash("Email already taken.", "register_error")
            is_valid=False
        # for passwords
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters long", "registration")
            is_valid=False
        if data['password'] != data['confirm_password']:
            flash("Passwords don't match.", "registration")
            is_valid=False
        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query, data)
        if len(results) == 0:
            flash("Email does not exist.", "login_error")
            is_valid=False
        if len(data['email']) == 0:
            flash("Email field cannot be empty", "login_error")
            is_valid=False
        if len(data['password']) == 0:
            flash("Password field cannot be empty", "login_error")
            is_valid=False
        # if not EMAIL_REGEX.match(email['email']):
        #     flash("Invalid Email!!!")
        #     is_valid=False
        return is_valid