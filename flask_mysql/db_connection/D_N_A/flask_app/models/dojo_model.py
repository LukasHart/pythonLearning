from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model

class Dojo:
    db = "dojos_and_ninjas_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
    @classmethod
    def save_dojo(cls,data):
        query = """
        INSERT INTO dojos (name)
        VALUES (%(name)s)
        ;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        return results
    
    @classmethod 
    def delete_dojo(cls,id):
        query = """
            DELETE FROM dojos
            WHERE id = %(id)s
        """
        data = {'id':id}
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_all_dojos(cls):
        query = """
            SELECT * FROM dojos;
        """
        results = connectToMySQL(cls.db).query_db(query)
        return [cls(result) for result in results]
    
    @classmethod
    def get_ninjas_by_dojo(cls,data):
        query = """
            SELECT * FROM dojos
            LEFT JOIN ninjas ON
            ninjas.dojo_id = dojos.id
            WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        dojo = cls(results[0])
        for row in results:
            data = {
                'id':row['ninjas.id'],
                'dojo_id':row['dojo_id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'age':row['age'],
                'created_at':row['ninjas.created_at'],
                'updated_at':row['ninjas.created_at']
            }
            dojo.ninjas.append(ninja_model.Ninja(data))
        return dojo