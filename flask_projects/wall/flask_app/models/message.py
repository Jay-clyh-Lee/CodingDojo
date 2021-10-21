from ..config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import user

class Message:
    db = "wall_schema"

    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None
        self.likers = []

    def __str__(self):
        return self.first_name

    def __repr__(self):
        return self.first_name

    @classmethod
    def create_message(cls, data):
        query = "INSERT INTO messages (content, user_id) VALUES (%(content)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM messages LEFT JOIN users ON users.id = user_id"\
    #             "ORDER BY messages.created_at DESC;"
                    
    #     results = connectToMySQL(cls.db).query_db(query) 
    #     messages = []
    #     for row in results:
    #         new_message = cls(row)
    #         user_data = { 
    #             'id': row['users.id'],
    #             'first_name': row['first_name'],
    #             'last_name': row['last_name'],
    #             'email': row['email'],  
    #             'password': row['password'],
    #             'created_at': row['users.created_at'],
    #             'updated_at': row['users.updated_at'],
    #         }
    #         new_message.user = user.User(user_data)
    #         messages.append(new_message)
    #     return messages

    @classmethod
    def get_message_by_id(cls, data):
        query = "SELECT * FROM messages WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def update_message(cls,data):
        query = "UPDATE messages SET content = %(content)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def destroy_message(cls,data):
        query = "DELETE FROM messages WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM messages LEFT JOIN users ON users.id = messages.user_id LEFT JOIN likes ON  messages.id = likes.message_id LEFT JOIN users AS likers ON likers.id = likes.user_id;"
        results = connectToMySQL(cls.db).query_db(query) 
        all_messages = []
        for row in results:
            # make a new instance of the message
            new_message = True
            #attn: it is a joint table and these below are class User Attributes
                # it is a dictionary of the user's info
            liker_data = { 
                'id': row['likers.id'],
                'first_name': row['likers.first_name'],
                'last_name': row['likers.last_name'],
                'email': row['likers.email'],  
                'password': row['likers.password'],
                'created_at': row['likers.created_at'],
                'updated_at': row['likers.updated_at'],
            }
            # if there's more likers on the last message, then it's not a new message
            if len(all_messages) > 0 and all_messages[-1].id == row['id']:
                all_messages[-1].likers.append(user.User(liker_data))
                new_message = False
            if new_message:
                # make a new user message object 
                this_message = cls(row)
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
                this_message.user = this_user
                #Q: is there still a person who likes this post?
                if row['likers.id'] is not None:
                    this_liker = user.User(liker_data)
                    this_message.likers.append(this_liker)
                all_messages.append(this_message)
        return all_messages

    @classmethod
    def like_message(cls, data):
        query = "INSERT INTO likes (user_id, message_id) VALUES (%(user_id)s, %(message_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def dislike_message(cls, data):
        query = "DELETE FROM likes WHERE message_id = %(message_id)s AND user_id = %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all_liked_messages(cls, data):
        liked_messages = []
        query = "SELECT message_id FROM likes JOIN users ON users.id = user_id WHERE user_id = %(user_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        for row in results:
            liked_messages.append(row['post_id'])
        return liked_messages


    @staticmethod
    def validate_message(data):
        is_valid = True
        if len(data["content"]) < 3:
            flash("Message must be at least 3 characters.", "message")
            is_valid=False
        return is_valid