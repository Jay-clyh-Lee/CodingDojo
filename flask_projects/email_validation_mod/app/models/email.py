from app.config.mysqlconnection import connectToMySQL
from flask import flash

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL('dojo_survey_schema').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        emails = []
        for email in emails:
            emails.append(cls(email))
        return emails

    @staticmethod
    def validate_email(email):
        is_valid = True
        if email 