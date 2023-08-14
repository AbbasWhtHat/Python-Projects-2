# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/index")
def home():

    name = "Abbas" # write your name
    age = "17" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name = "Father" # write your name
    age = "47" # write your age

    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "Mother" # write your name
    age = "45" # write your age

    return render_template('mother.html' , name = name , age = age) 

# define the route to friends webpage
@app.route("/friend")
def friend():

    name = "Yash" # write your name
    age = "17" # write your age

    return render_template('friend.html' , name = name , age = age)

# run the file
app.run(debug=True)
