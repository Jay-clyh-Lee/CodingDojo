from ..config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import user

conditions = ["hopelessness", "negative_thoughts", "cognitive_problems", "focus_problems", "restlessness", "poor_appetite", "worthlessness", "fatigue", "sleep_problems", "loss_of_interest" ]

class Test:
    db = "mental_health_awareness"

    def __init__(self, data):
        # id
        self.id = data['id']
        # test conditions. level: 1, 2, 3
        self.hopelessness = data["hopelessness"]
        self.negative_thoughts = data["negative_thoughts"]
        self.cognitive_problems = data["cognitive_problems"]
        self.focus_problems = data["focus_problems"]
        self.restlessness = data["restlessness"]
        self.poor_appetite = data["poor_appetite"]
        self.worthlessness = data["worthlessness"]
        self.fatigue = data["fatigue"]
        self.sleep_problems = data["sleep_problems"]
        self.loss_of_interest = data["loss_of_interest"]
        # test score (sum of condition levels)
        self.result = data['result']
        # other
        self.created_at = data['created_at']
        # test cannot be updated, only retakes
        # self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def create_test(cls, data):
        query = "INSERT INTO tests (hopelessness, negative_thoughts, cognitive_problems, focus_problems, restlessness, poor_appetite, worthlessness, fatigue, sleep_problems, loss_of_interest, result, user_id) VALUES (%(hopelessness)s, %(negative_thoughts)s, %(cognitive_problems)s, %(focus_problems)s, %(restlessness)s, %(poor_appetite)s, %(worthlessness)s, %(fatigue)s, %(sleep_problems)s, %(loss_of_interest)s, %(result)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)
        
    @classmethod
    def get_tests_by_user_id(cls, data):
        query = "SELECT * FROM tests LEFT JOIN users ON users.id = tests.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        my_tests = []
        for row in results:
            my_tests.append(cls(row))
        return my_tests

    @classmethod
    def get_test_by_id_simple(cls, data):
        query = "SELECT * FROM tests LEFT JOIN users ON users.id = tests.user_id WHERE tests.id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_by_test_id(cls, data):
        query = "SELECT * FROM tests LEFT JOIN users ON users.id = user_id WHERE tests.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data) 
        for row in results:
            new_test = cls(row)
            user_data = { 
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'email': row['email'],  
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            }
            new_test.user = user.User(user_data)
        return new_test

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tests LEFT JOIN users ON users.id = tests.user_id;"
        results = connectToMySQL(cls.db).query_db(query) 
        all_tests = []
        for row in results:
            this_test = cls(row)
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
            # now each test has an user attribute which are User instances
            this_test.user = user.User(user_data)
            # all tests
            all_tests.append(this_test)
        return all_tests

    # ideas for further development
    @classmethod
    # user cannot update test
    # update only for fixing typo or insert internal comment by doctors/admins
    def update_test(cls,data):
        query = "UPDATE tests SET hopelessness=%(hopelessness)s, negative_thoughts=%(negative_thoughts)s, cognitive_problems=%(cognitive_problems)s, focus_problems=%(focus_problems)s, restlessness=%(restlessness)s, poor_appetite=%(poor_appetite)s, worthlessness=%(worthlessness)s, fatigue=%(fatigue)s, user_id=%(user_id)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    # user cannot delete test except by admin
    def destroy_test(cls,data):
        query = "DELETE FROM tests WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)


    # Static
    # not needed since users must choose 1 out of 3 options for each condition
    @staticmethod
    def validate_test(data):
        is_valid = True
        if len(data["location"]) == 0:
            flash("Location cannot be empty.", "test")
            is_valid=False
        if len(data["description"]) == 0:
            flash("What happened cannot be empty.", "test")
            is_valid=False
        if data["date_sighted"] == "":
            flash("Select a date.", "test")
            is_valid=False
        if len(data["count"]) < 1:
            flash("Number of tests must be at least 1", "test")
            is_valid=False
        return is_valid