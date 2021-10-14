from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    db = "books_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = [] # attn;

    @classmethod
    def save(cls,data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls): #attn;
        query = "SELECT * FROM authors;"
        results = connectToMySQL(cls.db).query_db(query)
        authors = []
        for a in results:
            authors.append(cls(a))
        return authors

    @classmethod
    def unfavorited_authors(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        authors = []
        results = connectToMySQL(cls.db).query_db(query,data)
        for row in results:
            authors.append(cls(row))
        return authors

    @classmethod
    def add_favorite(cls, data):
        query = "INSERT INTO "