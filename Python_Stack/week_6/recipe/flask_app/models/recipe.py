from ..config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import user

class Recipe:
    db = "arbortrary"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.duration = data['duration']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    # def __str__(self):
    #     return self.first_name

    # def __repr__(self):
    #     return self.first_name

    @classmethod
    def create_recipe(cls, data):
        query = "INSERT INTO recipes (name, descriptions, duration, instruction, date_made, user_id) VALUES (%(name)s, %(descriptions)s, %(duration)s, %(instruction)s, %(date_made)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_recipe_by_id(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all_by_id(cls,data):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        recipes = []
        for row in results:
            recipe = cls(row)
            user_data = { 
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],  
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            }
            recipe.user = user.User(user_data)
            recipes.append(recipe)
        return recipes
        
    @classmethod
    def get_recipes_by_user_id(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        user_recipes = []
        for row in results:
            user_recipes.append(cls(row))
        return user_recipes

    @classmethod
    def update_recipe(cls,data):
        query = "UPDATE recipes SET name = %(name)s, descriptions=%(descriptions)s, duration = %(duration)s, instructions = %(instruction)s, date_made = %(date_made)s, WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def destroy_recipe(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(cls.db).query_db(query) 
        all_recipes = []
        for row in results:
            all_recipes.append(cls(row))
        return all_recipes


    # @classmethod
    # def get_all_by_id(cls,data):
    #     query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id LEFT JOIN likes ON  recipes.id = likes.recipe_id LEFT JOIN users AS likeors ON likeors.id = likes.user_id WHERE recipes.id = %(id)s;"
    #     results = connectToMySQL(cls.db).query_db(query,data) 
    #     all_recipes = []
    #     for row in results:
    #         # make a new instance of the recipe
    #         new_recipe = True
    #         #attn: it is a joint table and these below are class User Attributes
    #             # it is a dictionary of the user's info
    #         likeor_data = { 
    #             'id': row['likeors.id'],
    #             'first_name': row['likeors.first_name'],
    #             'last_name': row['likeors.last_name'],
    #             'email': row['likeors.email'],  
    #             'password': row['likeors.password'],
    #             'created_at': row['likeors.created_at'],
    #             'updated_at': row['likeors.updated_at'],
    #         }
    #         # if there's more likeors on the last like, then it's not a new like
    #         if len(all_recipes) > 0 and all_recipes[-1].id == row['id']:
    #             all_recipes[-1].likeors.append(user.User(likeor_data))
    #             new_recipe = False
    #         if new_recipe:
    #             # make a new user like object 
    #             this_recipe = cls(row)
    #             user_data = {
    #                 'id': row['users.id'],
    #                 'first_name': row['first_name'],
    #                 'last_name': row['last_name'],
    #                 'email': row['email'],  
    #                 'password': row['password'],
    #                 'created_at': row['users.created_at'],
    #                 'updated_at': row['users.updated_at'],
    #             }
    #             # create a user instance for this creator
    #             this_user = user.User(user_data)
    #             this_recipe.user = this_user
    #             #Q: is there still a person who likes this post?
    #             if row['likeors.id'] is not None:
    #                 this_likeor = user.User(likeor_data)
    #                 this_recipe.likeors.append(this_likeor)
    #             all_recipes.append(this_recipe)
    #     return all_recipes

    @classmethod
    def like_recipe(cls, data):
        query = "INSERT INTO likes (user_id, recipe_id) VALUES (%(user_id)s, %(recipe_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    # @classmethod
    # def unlike_recipe(cls, data):
    #     query = "DELETE FROM likes WHERE recipe_id = %(recipe_id)s AND user_id = %(user_id)s);"
    #     return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all_liked_recipes(cls, data):
        liked_recipes = []
        query = "SELECT recipe_id FROM likes JOIN users ON users.id = user_id WHERE user_id = %(user_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        for row in results:
            liked_recipes.append(row['recipe_id'])
        return liked_recipes


    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data["name"]) < 3:
            flash("Name must be at least 3 characters.", "recipe")
            is_valid=False
        if len(data["description"]) < 3:
            flash("Description must be at least 3 characters.", "recipe")
            is_valid=False
        if len(data["instruction"]) < 3:
            flash("Instruction must be at least 3 characters.", "recipe")
            is_valid=False
        if data["duration"] <= 0:
            flash('Not a valid time')
        # if len(data["duration"]) == 0:
        #     flash("duration cannot be empty.", "recipe")
        #     is_valid=False
        if data["date_made"] == "":
            flash("Select a date.", "recipe")
            is_valid=False
        return is_valid