from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo_model

class Ninja:
    db = "dojos_and_ninjas_schema"
    def __init__(self,data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save_ninja(cls,data):
        query = """
            INSERT INTO ninjas (dojo_id,first_name,last_name,age)
            VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s)
            ;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        return results
    
    @classmethod
    def delete_ninja_by_id(cls,id):
        query = """
            DELETE FROM ninjas
            WHERE id = %(id)s
        """
        data = {'id':id}
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod 
    def get_ninjas_by_id(cls,id):
        query = """
            SELECT * FROM ninjas 
            WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,id)
        return cls(results[0])
    
    @classmethod
    def update_ninja(cls,data):
        query = """
        UPDATE ninjas
        SET first_name = %(first_name)s,
        last_name = %(last_name)s,
        age = %(age)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query,data)