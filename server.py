from flask import Flask, render_template, request, redirect
# import the class from user.py
from users import User
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    all_users=User.get_all()
    print(users)
    return render_template("read.html", users=all_users)

@app.route('/user/show/<int:user_id>')
def show(user_id):
    # calling the get_one method and supplying it with the id of the user we want to get
    user=User.get_one(user_id)
    return render_template("read.html",user=user)

@app.route('/create_user', methods=["POST"])
def create_user():
    # create processes form and redirects to the main page. this is where users input information
    # to POST
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    # Inserting data into a dictionary
    # data = {
    #     # "user_id": request.form["user_id"],
    #     "first_name": request.form["first_name"],
    #     "last_name" : request.form["last_name"],
    #     "email" : request.form["email"],
        # "created_at": request.form["created_at"]
    # }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(request.form)
    # Don't forget to redirect after saving to the database.
    return redirect('/')





if __name__ == "__main__":
    app.run(debug=True)

