# app.py
# Flask Flash Messages

# Import the necessary modules
from flask import Flask, render_template, request, url_for, redirect
from flask import flash

# An instance of Flask is created to initialize the Flask application.
app = Flask(__name__)

# Secret Key used for session management
app.secret_key = "Big Mike likes HTML5"

@app.route('/')
def index():
    return render_template('index.html')


'''The route "/info" is created to manage both GET and POST requests,
   and it is linked to the add_info() view function.'''
@app.route('/info/', methods=["GET", "POST"])
def add_info():
    if request.method == "POST":
        name = request.form['name']
        profession = request.form['profession']
 
        if name == "" or profession == "":
            flash("Invalid: Every field is required.")
            return redirect(url_for("add_info"))
        else:
            flash("Success: Info added successfully.")
            return redirect(url_for("add_info"))
    return render_template('info.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

