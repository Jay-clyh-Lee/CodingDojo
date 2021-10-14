from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    db = "books_schema"
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.pages = data['pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors_who_favorited = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO books (title, pages, created_at, updated_at) VALUES (%(title)s, %(pages)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls): #attn;
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.db).query_db(query)
        books = []
        for a in results:
            books.append(cls(a))
        return books

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorite ON books.id = favorite.book_id LEFT JOIN authors ON authors.id = favorite.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)

        book = cls(results[0])

        for row in results:
            if row['authors.id'] == None:
                break
            data = {
                "id": row['authors.id'],
                "name": row['name'], #'authors.name' or 'name' both work b/c only 1 col attr is name
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            book.authors_who_favorited.append(author.Author(data))
            return book

    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
        results = connectToMySQL('books').query_db(query,data)
        books = []
        for row in results:
            books.append(cls(row))
        print(books)
        return books