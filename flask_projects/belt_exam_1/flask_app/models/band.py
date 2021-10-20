from ..config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import user
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# NAME_REGEX = re.compile(r'^[a-zA-Z]+[a-zA-Z]$')

class Band:
    db = "band_together"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.genre = data['genre']
        self.home_city = data['home_city']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None
        
    @classmethod
    def create_band(cls, data):
        query = "INSERT INTO bands (name, genre, home_city, user_id) VALUES (%(name)s, %(genre)s, %(home_city)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)
#########
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM bands LEFT JOIN users ON users.id = user_id;"
        results = connectToMySQL(cls.db).query_db(query) 
        bands = []
        for row in results:
            # make a new instance of the band
            new_band = cls(row)
            #attn: it is a joint table and these below are class User Attributes
                # it is a dictionary of the user's info
            user_data = { 
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],  
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            }
            # make a new user object using "user_data"
            this_user = user.User(user_data)
            # make this user as an attribute of the message
            new_band.user = this_user
            bands.append(new_band)
        return bands

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM bands LEFT JOIN users ON bands.user_id = users.id WHERE bands.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE bands SET name=%(name)s, genre=%(genre)s, home_city=%(home_city)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM bands WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_band(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Name field must contain at least 2 characters.", "band")
            is_valid=False
        if len(data['genre']) < 3:
            flash("Genre field must contain at least 2 characters.", "band")
        is_valid=False
        if data['home_city'] == "":
            flash("City field cannot be empty.", "band")
        is_valid=False
        return is_valid