from app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.comment = data['comment']    
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name, location, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(comment)s, NOW(), NOW());'
        return connectToMySQL('dojo_survey_schema').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM surveys'
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        surveys = []
        for u in results:
            surveys.append(cls(u))
        return surveys

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM surveys WHERE id = %(id)s'
        result = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = 'UPDATE surveys SET name=%(name)s, location=%(location)s, comment=%(comment)s, updated_at=NOW() WHERE id=%(id)s;'
        return connectToMySQL('dojo_survey_schema').query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = 'DELETE FROM surveys WHERE id=%(id)s;'
        return connectToMySQL('dojo_survey_schema').query_db(query, data)

    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(survey['location']) < 3:
            flash("location must be a valid location name.")
            is_valid = False
        return is_valid