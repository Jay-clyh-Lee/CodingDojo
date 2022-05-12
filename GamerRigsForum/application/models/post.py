from config.mysqlconnection import connectToMySQL
from user import User
from flask import flash

class Post:

    db = "gamer_rigs_forum"
    
    def __init__(self, data):
        self.comment = data['comment']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_and_likers = None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts VALUES (comment, user_id) %(comment)s, %(user_id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE posts SET comment = %(comment)s WHERE posts.id = %(id)s"
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
