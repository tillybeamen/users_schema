# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database

DATABASE = "users_schema"

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append( cls(user))
        return users
    
    @classmethod
    def get_one(cls, user_id):
        query  = "SELECT * FROM users WHERE id = %(id)s"
        data = {'id':user_id}
        results = connectToMySQL(cls.DATABASE).query_db(query, data)
        return cls(results[0])

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( user_id, first_name , last_name , email, created_at ) VALUES ( %(user_id)s, %(first_name)s , %(last_name)s , %(email)s, %(created_at)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db( query, data )