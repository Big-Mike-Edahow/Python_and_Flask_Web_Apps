# app.py
# Geek for Geeks SQLAlchemy Tuturial

from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Big Mike prefers to code Python on Debian Linux.'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
# Create SQLAlchemy Instance
db = SQLAlchemy(app)
# Create Migrate Instance
migrate = Migrate(app, db)

# Models
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
 
    # repr method represents how one object of this datatable will look like
    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"
    
# Creating Database with App Context
def create_db():
    with app.app_context():
        db.create_all()

 
@app.route('/')
def index():
    # Query all data and then pass it to the template
    profiles = Profile.query.all()
    return render_template('index.html', profiles=profiles)

@app.route('/add_data')
def add_data():
    return render_template('add_profile.html')

# function to add profiles
@app.route('/add', methods=["POST"])
def profile():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    age = request.form.get("age")
 
    # Create an object of the Profile class of models
    # and store data as a row in our datatable
    if first_name != '' and last_name != '' and age is not None:
        p = Profile(first_name=first_name, last_name=last_name, age=age)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/')
    
@app.route('/delete/<int:id>')
def erase(id):
    # Deletes the data on the basis of unique id and 
    # redirects to home page
    data = Profile.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')
 
 
if __name__ == '__main__':
    create_db()
    app.run(debug=True)

