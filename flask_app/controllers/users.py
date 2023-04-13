# burgers.py
from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User




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

# CREATE

@app.route('/users/create/', methods=["POST"])
def create():
    print(request.form)
    # create processes form and redirects to the main page. this is where users input information
    # to POST
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    # Inserting data into a dictionary
    # We pass the data dictionary into the save method from the Friend class.
    User.save(request.form)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

# READ ONE

@app.route('/users/edit/<int:id>') # when you declare a variable here, it must be passed down to function
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


# UPDATE

@app.route('/users/update/', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')


# DELETE

@app.route('/users/destroy/<int:id>')
def destroy(id):
    data = {
        'id':id
    }
    User.destroy(data)
    return redirect('/users')
