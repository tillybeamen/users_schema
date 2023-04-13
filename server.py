# import the class from user.py
from flask_app.controllers.users import app, User
from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection



# app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

