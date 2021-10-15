from ..config.mysqlconnection import connectToMySQL
from flask import flash
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
        self.message_id = data['message_id']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO comments (content, message_id, user_id) VALUES (%(content)s, %(message_id)s, %(user_id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

