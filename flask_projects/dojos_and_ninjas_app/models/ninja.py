from dojos_and_ninjas_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age= db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # We create a list so that later we can add in all the ninjas that are associated with a restaurant.
        self.ninjas = []

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO dojos ( first_name , last_name, age, dojo_id, created_at , updated_at ) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(),NOW());"
        return connectToMySQL('ninjas').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for u in results:
            ninjas.append( cls(u) )
        return ninjas

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM ninjas WHERE id = %(id)s";
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name=%(first_name)s,last_name=%(last_name)s,age=%(age)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)