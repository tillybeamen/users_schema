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

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Now we use class methods to query our database

    # READ ALL

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append( cls(user))
        return users
    
    # CREATE

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email ) VALUES (%(first_name)s , %(last_name)s , %(email)s);"

        # comes back as the new row id
        # if query is bad it will comeb ack as false
        # data is a dictionary that will be passed into the save method from server.py
         
        return connectToMySQL(DATABASE).query_db(query, data)
    

    # READ ONE

    @classmethod
    def get_one(cls, data):
        query  = "SELECT * FROM users WHERE id = %(id)s"
        # data = {'id':user_id}
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])
    
    # UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id = %(id)s; "
        return connectToMySQL('users_schema').query_db(query,data)

    # DELETE
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)