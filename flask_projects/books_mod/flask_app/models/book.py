from config.mysqlconnection import connectToMySQL

class Book:
    db = "books_schema"
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.pages = data['pages']
        self.created_at = data['created_at']
        self.udpated_at = data['udpated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO books (title, pages, created_at, updated_at) VALUES (%(title)s, %(pages)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        return connectToMySQL(cls.db).query_db(query)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)