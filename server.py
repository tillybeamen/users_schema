from flask import Flask, render_template, request, redirect
# import the class from user.py
from users import User
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all users

    return redirect('/users')

@app.route('/users')
def users():
    # calling the get_one method and supplying it with the id of the user we want to get
    
    return render_template("users.html",users=User.get_all())


@app.route('/users/new/')
def new():
    return render_template('new_user.html')



@app.route('/users/create/', methods=["POST"])
def create():
    print(request.form)
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
    return redirect('/users')

@app.route('/users/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }   
    return render_template("edit_user.html",user=User.get_one(data))

@app.route('/users/show/<int:id>')
def show(id):
    data = {
        "id":id
    }   
    return render_template("show_user.html",user=User.get_one(data))

@app.route('/users/update/', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/users/destroy/<int:id>')
def destroy(id):
    data = {
        'id':id
    }
    User.destroy(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)

