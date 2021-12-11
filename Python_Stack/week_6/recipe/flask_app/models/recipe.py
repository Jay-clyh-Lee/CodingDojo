from ..config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import user

class recipe:
    db = "arbortrary"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.duration = data['duration']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None
        self.visitors = []

    # def __str__(self):
    #     return self.first_name

    # def __repr__(self):
    #     return self.first_name

    @classmethod
    def create_recipe(cls, data):
        query = "INSERT INTO recipes (species, locations, reasons, date_planted, user_id) VALUES (%(species)s, %(locations)s, %(reasons)s, %(date_planted)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_recipe_by_id(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all_by_id(cls,data):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data) 
        for row in results:
            new_recipe = cls(row)
            user_data = { 
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],  
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            }
            new_recipe.user = user.User(user_data)
        return new_recipe
        
    @classmethod
    def get_my_recipes(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        my_recipes = []
        for row in results:
            my_recipes.append(cls(row))
        return my_recipes

    @classmethod
    def update_recipe(cls,data):
        query = "UPDATE recipes SET species = %(species)s, locations=%(locations)s, reasons = %(reasons)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def destroy_recipe(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id LEFT JOIN visits ON  recipes.id = visits.recipe_id LEFT JOIN users AS visitors ON visitors.id = visits.user_id;"
        results = connectToMySQL(cls.db).query_db(query) 
        all_recipes = []
        for row in results:
            # make a new instance of the recipe
            new_recipe = True
            #attn: it is a joint table and these below are class User Attributes
                # it is a dictionary of the user's info
            visitor_data = { 
                'id': row['visitors.id'],
                'first_name': row['visitors.first_name'],
                'last_name': row['visitors.last_name'],
                'email': row['visitors.email'],  
                'password': row['visitors.password'],
                'created_at': row['visitors.created_at'],
                'updated_at': row['visitors.updated_at'],
            }
            # if there's more visitors on the last visit, then it's not a new visit
            if len(all_recipes) > 0 and all_recipes[-1].id == row['id']:
                all_recipes[-1].visitors.append(user.User(visitor_data))
                new_recipe = False
            if new_recipe:
                # make a new user visit object 
                this_recipe = cls(row)
                user_data = {
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],  
                    'password': row['password'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at'],
                }
                # create a user instance for this creator
                this_user = user.User(user_data)
                this_recipe.user = this_user
                #Q: is there still a person who visits this post?
                if row['visitors.id'] is not None:
                    this_visitor = user.User(visitor_data)
                    this_recipe.visitors.append(this_visitor)
                all_recipes.append(this_recipe)
        return all_recipes



    # @classmethod
    # def get_all_by_id(cls,data):
    #     query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id LEFT JOIN visits ON  recipes.id = visits.recipe_id LEFT JOIN users AS visitors ON visitors.id = visits.user_id WHERE recipes.id = %(id)s;"
    #     results = connectToMySQL(cls.db).query_db(query,data) 
    #     all_recipes = []
    #     for row in results:
    #         # make a new instance of the recipe
    #         new_recipe = True
    #         #attn: it is a joint table and these below are class User Attributes
    #             # it is a dictionary of the user's info
    #         visitor_data = { 
    #             'id': row['visitors.id'],
    #             'first_name': row['visitors.first_name'],
    #             'last_name': row['visitors.last_name'],
    #             'email': row['visitors.email'],  
    #             'password': row['visitors.password'],
    #             'created_at': row['visitors.created_at'],
    #             'updated_at': row['visitors.updated_at'],
    #         }
    #         # if there's more visitors on the last visit, then it's not a new visit
    #         if len(all_recipes) > 0 and all_recipes[-1].id == row['id']:
    #             all_recipes[-1].visitors.append(user.User(visitor_data))
    #             new_recipe = False
    #         if new_recipe:
    #             # make a new user visit object 
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
    #             #Q: is there still a person who visits this post?
    #             if row['visitors.id'] is not None:
    #                 this_visitor = user.User(visitor_data)
    #                 this_recipe.visitors.append(this_visitor)
    #             all_recipes.append(this_recipe)
    #     return all_recipes

    @classmethod
    def visit_recipe(cls, data):
        query = "INSERT INTO visits (user_id, recipe_id) VALUES (%(user_id)s, %(recipe_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    # @classmethod
    # def unvisit_recipe(cls, data):
    #     query = "DELETE FROM visits WHERE recipe_id = %(recipe_id)s AND user_id = %(user_id)s);"
    #     return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all_visited_recipes(cls, data):
        visited_recipes = []
        query = "SELECT recipe_id FROM visits JOIN users ON users.id = user_id WHERE user_id = %(user_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        for row in results:
            visited_recipes.append(row['post_id'])
        return visited_recipes


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
        if data["duration"] > 0 and data["duration"] < 30:
            flash('not valid')
        # if len(data["reasons"]) == 0:
        #     flash("Reasons cannot be empty.", "recipe")
        #     is_valid=False
        if data["date_made"] == "":
            flash("Select a date.", "recipe")
            is_valid=False
        return is_valid