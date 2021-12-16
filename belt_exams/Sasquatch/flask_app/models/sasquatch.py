from ..config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import user

class Sasquatch:
    db = "sasquatch"

    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.description = data['description']
        self.date_sighted = data['date_sighted']
        self.count = data['count']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def create_sasquatch(cls, data):
        query = "INSERT INTO sasquatches (location, description, date_sighted, count, user_id) VALUES (%(location)s, %(description)s, %(date_sighted)s, %(count)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_sasquatch_by_id(cls, data):
        query = "SELECT * FROM sasquatches WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
        
    @classmethod
    def get_my_sasquatches(cls, data):
        query = "SELECT * FROM sasquatches LEFT JOIN users ON users.id = sasquatches.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        my_sasquatches = []
        for row in results:
            my_sasquatches.append(cls(row))
        return my_sasquatches

    @classmethod
    def update_sasquatch(cls,data):
        query = "UPDATE sasquatches SET location=%(location)s, description=%(description)s, date_sighted=%(date_sighted)s, count=%(count)s, user_id=%(user_id)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def destroy_sasquatch(cls,data):
        query = "DELETE FROM sasquatches WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sasquatches LEFT JOIN users ON users.id = sasquatches.user_id;"
        results = connectToMySQL(cls.db).query_db(query) 
        all_sasquatches = []
        for row in results:
            this_sasquatch = cls(row)
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
            this_sasquatch.user = this_user
            all_sasquatches.append(this_sasquatch)
        return all_sasquatches

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM sasquatches LEFT JOIN users ON users.id = user_id WHERE sasquatches.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data) 
        for row in results:
            new_sasquatch = cls(row)
            user_data = { 
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],  
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            }
            new_sasquatch.user = user.User(user_data)
        return new_sasquatch


    @staticmethod
    def validate_sasquatch(data):
        is_valid = True
        if len(data["location"]) == 0:
            flash("Location cannot be empty.", "sasquatch")
            is_valid=False
        if len(data["description"]) == 0:
            flash("What happened cannot be empty.", "sasquatch")
            is_valid=False
        if data["date_sighted"] == "":
            flash("Select a date.", "sasquatch")
            is_valid=False
        if len(data["count"]) < 1:
            flash("Number of sasquatches must be at least 1", "sasquatch")
            is_valid=False
        return is_valid