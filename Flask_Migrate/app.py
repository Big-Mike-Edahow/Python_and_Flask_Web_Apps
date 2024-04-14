# app.py
# Flask-SQLAlchemy and Flask-Migrate

from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create Flask App Instance
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Big Mike likes to keep things simple.'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
# Create SQLAlchemy Database Instance
db = SQLAlchemy(app)
# Create Migration Engine Instance
migrate = Migrate(app, db)

# Database Models
class Vehicle(db.Model):
    __tablename__ = "vehicle"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())
    
# Create Database with App Context
def create_db():
    with app.app_context():
        db.create_all()

# Routes
@app.route("/")
def index():
    details = Vehicle.query.all()
    return render_template("index.html", details=details)
 
@app.route("/add-vehicle", methods=['GET', 'POST'])
def add_vehicle():
    if request.method == 'POST':
        v_name = request.form.get('vehicle')
        price = request.form.get('price')
 
        add_detail = Vehicle(
            name=v_name,
            price=price
        )
        db.session.add(add_detail)
        db.session.commit()
        return redirect(url_for('index'))
 
    return render_template("add_vehicle.html")

@app.route('/delete/<int:id>')
def erase(id):
    # Deletes the data on the basis of unique id and 
    # redirects to home page
    data = Vehicle.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')

@app.route('/about')
def about():
    return render_template("about.html")


# Run Main Program
if __name__ == "__main__":
    create_db()
    app.run(debug=True)

