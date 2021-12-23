from ..config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Painting:
    db = "paintings"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.price = data['price']
        self.quantity = data['quantity']
        self.sold = data['sold']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None
        self.buyers = []

    @classmethod
    def create_painting(cls, data):
        query = "INSERT INTO paintings (name, description, price, quantity, user_id) VALUES (%(name)s, %(description)s, %(price)s, %(quantity)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_painting_by_id(cls, data):
        query = "SELECT * FROM paintings WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
        
    @classmethod
    def get_my_paintings(cls, data):
        query = "SELECT * FROM paintings LEFT JOIN users ON users.id = paintings.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        my_paintings = []
        for row in results:
            my_paintings.append(cls(row))
        return my_paintings

    @classmethod
    def update_painting(cls,data):
        query = "UPDATE paintings SET name=%(name)s, description=%(description)s, price=%(price)s, quantity=%(quantity)s, user_id=%(user_id)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def destroy_painting(cls,data):
        query = "DELETE FROM paintings WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM paintings LEFT JOIN users ON users.id = paintings.user_id;"
        results = connectToMySQL(cls.db).query_db(query) 
        all_paintings = []
        for row in results:
            this_painting = cls(row)
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
            this_painting.user = this_user
            all_paintings.append(this_painting)
        return all_paintings

    @classmethod
    def get_all_detailed(cls):
        query = "SELECT * FROM paintings LEFT JOIN users ON users.id = paintings.user_id LEFT JOIN purchases ON paintings.id = purchases.painting_id LEFT JOIN users AS buyers ON buyers.id = purchases.user_id;"
        results = connectToMySQL(cls.db).query_db(query) 
        all_paintings = []
        for row in results:
            this_painting = cls(row)
            buyer_data = { 
                'id': row['buyers.id'],
                'first_name': row['buyers.first_name'],
                'last_name': row['buyers.last_name'],
                'email': row['buyers.email'],  
                'password': row['buyers.password'],
                'created_at': row['buyers.created_at'],
                'updated_at': row['buyers.updated_at'],
            }
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],  
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            }
            this_user = user.User(user_data)
            this_painting.user = this_user
            this_buyer = user.User(buyer_data)
            this_painting.buyers.append(this_buyer)
            # if row['buyers.id'] is not None:
                
            all_paintings.append(this_painting)
        return all_paintings

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT DISTINCT * FROM paintings LEFT JOIN users ON users.id = paintings.user_id LEFT JOIN purchases ON paintings.id = purchases.painting_id LEFT JOIN users AS buyers ON buyers.id = purchases.user_id WHERE paintings.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)    
        this_painting = cls(results[0])
        artist_data = { 
            'id': results[0]['users.id'],
            'first_name': results[0]['first_name'],
            'last_name': results[0]['last_name'],
            'email': results[0]['email'],
            'password': results[0]['password'],
            'created_at': results[0]['users.created_at'],
            'updated_at': results[0]['users.updated_at'],
        }
        this_painting.user = user.User(artist_data)
        for row in results:
            buyer_data = { 
                'id': row['buyers.id'],
                'first_name': row['buyers.first_name'],
                'last_name': row['buyers.last_name'],
                'email': row['buyers.email'],  
                'password': row['buyers.password'],
                'created_at': row['buyers.created_at'],
                'updated_at': row['buyers.updated_at'],
            }
            this_painting.buyers.append(buyer_data)
        return this_painting

    @classmethod
    def buy_painting(cls, data):
        query = "INSERT INTO purchases (painting_id, user_id) VALUES (%(painting_id)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_my_purchased_paintings(cls, data):
        purchased_paintings = []
        query = "SELECT * FROM users JOIN purchases ON purchases.user_id = users.id JOIN paintings ON purchases.painting_id = paintings.id WHERE users.id = %(user_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False 
        for row in results:
            purchased_paintings.append(cls(row))
        return purchased_paintings


    @staticmethod
    def validate_painting(data):
        is_valid = True
        if len(data["name"]) < 2:
            flash("Title should be at least 2 characters long.", "painting")
            is_valid=False
        if len(data["description"]) < 10:
            flash("Descriptoin should be at least 10 characters long.", "painting")
            is_valid=False
        if len(data["price"]) == 0 or float(data["price"]) <= 0:
            flash("Price should be greater than 0.", "painting")
            is_valid=False
        if len(data["quantity"]) == 0 or int(data["quantity"]) < 1:
            flash("Quantity should be greater than 0.", "painting")
            is_valid=False
        return is_valid