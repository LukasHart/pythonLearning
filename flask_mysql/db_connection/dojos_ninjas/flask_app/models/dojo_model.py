from flask_app.config.mysqlconnection import connectToMySQL

from .ninja_model import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_one_dojo(cls,id):
        query = 'SELECT * FROM dojos WHERE ID = %(id)s;'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,id)
    
    @classmethod
    def save_dojo(cls,data):
        query = 'INSERT INTO dojos (name, location, created_at, updated_at) VALUES (%(name)s,%(location)s, NOW(),NOW());'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    
    @classmethod 
    def get_ninjas(cls,data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        dojo = cls(results[0])
        for rows in results:
            info = {
                'id': rows ['ninjas.id'],
                'dojo_id': rows['dojo_id'],
                'first_name': rows['first_name'],
                'last_name': rows['last_name'],
                'age': rows ['age'],
                'created_at': rows['ninjas.created_at'],
                'updated_at': rows['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(info))
        return dojo
