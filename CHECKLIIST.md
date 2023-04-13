- [x] create a new directory
- [x] inside the directory create virtual env by running:
  
'''bash
[python -m] pipenv install flask



pipenv install flask pymysql #this connects flask app to mysql



create [mysqlconnection.py]
### add this to the file ###
# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = False)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query:str, data:dict=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
     
                cursor.execute(query)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)



create [book.py]
### add this to the top ###
# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
'''


- [x] activate the virtual env every time you open a new terminal:
  
  '''bash
  [python -m] pipenv shell
  '''

- [x] create [server.py](server.py)

'''py
from flask import Flask, render_template, redirect, session, request #import flask to allow us to create our app

app = Flask(__name__)
app.secret_key = "any string you want"

@app.route('/')        #the "@" decorator associates this route with the function imeediately following
def index():
    return render_template('index.html')  

@app.route('/handle_form', methods=['POST'])
def create():
    ## code to process date from form
    return redirect('/')  # always redirect to a route

@app.route('/show')
    def show():

        return render_template('show.html')

if __name__=="__main__":     # Ensure this file is being run directly and not from a different module
    app.run(debug=True)     # Run the app in debug mode.

- [x] start app by running python server.py