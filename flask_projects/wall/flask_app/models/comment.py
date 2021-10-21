from ..config.mysqlconnection import connectToMySQL
from flask import flash

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
    def create_comment(cls, data):
        query = "INSERT INTO comments (content, message_id, user_id) VALUES (%(content)s, %(message_id)s, %(user_id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

