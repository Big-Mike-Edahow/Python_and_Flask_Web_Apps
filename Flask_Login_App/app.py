# app.py
# Geeks_for_Geeks Flask-Login App

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user
 
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "It's snowing and blowing outside"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)
 
login_manager = LoginManager()
login_manager.init_app(app)

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)


# Create Database with App Context
def create_db():
    with app.app_context():
        db.create_all()

 
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = Users(username=request.form.get("username"),
                     password=request.form.get("password"))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("sign_up.html")
 
 
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Users.query.filter_by(
            username=request.form.get("username")).first()
        if user.password == request.form.get("password"):
            login_user(user)
            return redirect(url_for("index"))
    return render_template("login.html")
 
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template('about.html')
 
 
# Run Main Program
if __name__ == "__main__":
    create_db()
    app.run(debug=True)

