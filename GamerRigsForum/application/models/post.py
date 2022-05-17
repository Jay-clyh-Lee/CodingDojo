from config.mysqlconnection import connectToMySQL
from application.models import user
from flask import flash

class Post:

    db = "gamer_rigs_forum"
    
    def __init__(self, data):
        self.comment = data['comment']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
        self.likers = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts VALUES (comment, user_id) %(comment)s, %(user_id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE posts SET comment = %(comment)s, user_id = %(user_id)s WHERE posts.id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM posts WHERE posts.id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_posts_with_user(cls, data):
        query = "SELECT * FROM posts LEFT JOIN users ON posts.user_id = posts.id WHERE posts.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)         
        posts = []
        for row in results:
            posts.append(cls(row))
            user_data = {
                "id" : row["user_id"],
            }
            # posts.append(User.get_user(user_data))
        return posts

    @classmethod
    def get_post_by_user(cls, data):
        query = "SELECT * FROM posts LEFT JOIN users ON users.id = posts.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        posts_by_this_user = []
        for row in results:
            posts_by_this_user.append(cls(row))
        return posts_by_this_user

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts LEFT JOIN users ON users.id = posts.user_id;"
        results = connectToMySQL(cls.db).query_db(query) 
        all_posts = []
        for row in results:
            this_post = cls(row)
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
            this_post.user = this_user
            all_posts.append(this_post)
        return all_posts

    @classmethod
    def get_all_detailed(cls):
        query = "SELECT * FROM posts LEFT JOIN users ON users.id = posts.user_id LEFT JOIN likes ON posts.id = likes.painting_id LEFT JOIN users AS likers ON likers.id = likes.user_id;"
        results = connectToMySQL(cls.db).query_db(query) 
        all_posts = []
        for row in results:
            this_post = cls(row)
            liker_data = { 
                'id': row['likers.id'],
                'first_name': row['likers.first_name'],
                'last_name': row['likers.last_name'],
                'email': row['likers.email'],  
                'password': row['likers.password'],
                'created_at': row['likers.created_at'],
                'updated_at': row['likers.updated_at'],
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
            this_post.user = this_user
            this_liker = user.User(liker_data)
            this_post.likers.append(this_liker)
            # if row['likers.id'] is not None:
                
            all_posts.append(this_post)
        return all_posts

    @classmethod
    def get_user_and_liked_posts_(cls, data):
        get_user_liked_posts = []
        query = "SELECT * FROM users JOIN likes ON likes.user_id = users.id JOIN posts ON likes.post_id = posts.id WHERE users.id = %(user_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False 
        for row in results:
            get_user_liked_posts.append(cls(row))
        return get_user_liked_posts

    @classmethod
    def like_post(cls, data):
        query = "INSERT INTO likes (user_id, post_id) VALUES (%(user_id)s, %(post_id)s)"
        return connectToMySQL(cls.db).query_db(query, data)     
    
    @classmethod
    def get_post_user_and_liker(cls, data):
        query = "SELECT * FROM posts LEFT JOIN users ON posts.user_id = posts.id LEFT JOIN likers ON likers.post_id = posts.id WHERE posts.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        this_post = []
        user_data = {
                "id": row["users.id"],
            #     "first_name": row["first_name"],
            #     "last_name": row["last_name"],
            #     "email": row["email"],
            #     "password": row["password"],
            }
        user = User.get_user(user_data)
        likers = []
        for row in results:
            liker_data = {
                # "first_name": row["likers.first_name"],
                # "last_name": row["likers.last_name"],
                # "email": row["likers.email"],
                # "password": row["likers.password"],
                "user_id": row["likers.user_id"],
                # "post_id": row["likers.post_id"],
            }    
            likers.append(User.get_user(liker_data))
        this_post.append(user)
        this_post += likers
        return this_post


    @staticmethod
    #valid post
    ## add profanity filter API
    def validate_post(form_data):
        is_valid = True
        if form_data['comment'] < 30:
            flash("At least 30 characters are required.", "post")
            is_valid = False
        return is_valid
