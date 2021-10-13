from config.mysqlconnection import connectToMySQL

class Book:
    db = "books_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.udpated_at = data['udpated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        return connectToMySQL(cls.db).query_db(query)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM author WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)