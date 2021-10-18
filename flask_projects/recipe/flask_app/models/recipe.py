from ..config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import user
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+[a-zA-Z]$')

class Recipe:
    db = "recipe_schema"

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.details = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def create_recipe(cls, data):
        query = "INSERT INTO recipes (title, details) VALUES (%(title)s, %(details)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all_by_user_id(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data) 
        recipes = []
        for row in results:
            recipes.append(cls(row))
            # a_new_recipe = cls(row)
            # user_data = { 
            #     'id': row['users.id'],
            #     'first_name': row['first_name'],
            #     'last_name': row['last_name'],
            #     'email': row['email'],  
            #     'password': row['password'],
            #     'created_at': row['users.created_at'],
            #     'updated_at': row['users.updated_at'],
            # }
            # this_user = user.User(user_data)
            # a_new_recipe.writer = this_user
            # recipes.append(a_new_recipe)
        return recipes

    @classmethod
    def get_all_by_user(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE u;"
        results = connectToMySQL(cls.db).query_db(query) 
        recipes = []
        for u in results:
            recipes.append(cls(u))
        return recipes


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
    def get_by_id(cls,data):
        query = "SELECT * FROM users LEFT JOIN messages ON messages.user_id = users.id LEFT JOIN comments ON comments.user_id = users.id WHERE users.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])


    @classmethod
    def update(cls, data):
        query = "UPDATE users SET (first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, password=%(password)s, updated_at=NOW());"
        return connectToMySQL(cls.db).query_db(query,data)

