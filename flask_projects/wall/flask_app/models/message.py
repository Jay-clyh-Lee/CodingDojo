from ..config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import user
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Message:
    db = "wall_schema"

    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None # empty object attribute
        self.likers = [] # a list of objects

    @classmethod
    def create_message(cls, data):
        query = "INSERT INTO messages (content, user_id) VALUES (%(content)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM messages LEFT JOIN users ON users.id = user_id;"
    #     results = connectToMySQL(cls.db).query_db(query) 
    #     messages = []
    #     for row in results:
    #         # make a new instance of the message
    #         new_message = cls(row)
    #         #attn: it is a joint table and these below are class User Attributes
    #             # it is a dictionary of the user's info
    #         user_data = { 
    #             'id': row['users.id'],
    #             'first_name': row['first_name'],
    #             'last_name': row['last_name'],
    #             'email': row['email'],  
    #             'password': row['password'],
    #             'created_at': row['users.created_at'],
    #             'updated_at': row['users.updated_at'],
    #         }
    #         # make a new user object using "user_data"
    #         this_user = user.User(user_data)
    #         # make this user as an attribute of the message
    #         new_message.user = this_user
    #         new_message.user = user.User(user_data)
    #         messages.append(new_message)
    #     return messages

    @classmethod
    def like_message(cls, data):
        query = "INSERT INTO likes (user_id, message_id) VALUES (%(user_id)s, %(message_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def destroy_message(cls,data):
        query = "DELETE FROM messages WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM messages LEFT JOIN users ON users.id = messages.user_id LEFT JOIN likes ON likes.message_id = messages.id;"
        results = connectToMySQL(cls.db).query_db(query) 
        all_messages = []
        for row in results:
            # make a new instance of the message
            new_message = True
            #attn: it is a joint table and these below are class User Attributes
                # it is a dictionary of the user's info
            liker_data = { 
                'id': row['likes.id'],
                'first_name': row['likes.first_name'],
                'last_name': row['likes.last_name'],
                'email': row['likes.email'],  
                'password': row['likes.password'],
                'created_at': row['likes.created_at'],
                'updated_at': row['likes.updated_at'],
            }
            if len(all_messages) > 0 and all_messages[-1].id == row['id']:
                all_messages[-1].likes.append(user.User(liker_data))
                new_message = False
            if new_message:
                # make a new user object 
                this_message = cls(row)
                creator_data = {
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],  
                    'password': row['password'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at'],
                }
                # create a user instance for creator
                this_creator = user.User(creator_data)
                this_message.creator = this_creator
                #Q: is there  still a person who likes this post?
                if row['likes.id'] is not None:
                    this_liker = user.User(liker_data)
                    this_message.likers.append(this_liker)
        return all_messages