# app.py
# Geek Python MySQL Tutorial

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from init_db import SQLALCHEMY_DATABASE_URI
 
# Creating Flask app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 
# Creating SQLAlchemy instance
db = SQLAlchemy()
# Initializing Flask app with SQLAlchemy
db.init_app(app)

# Database Models
class Books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, unique=True)
    author = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())


def create_db():
    with app.app_context():
        db.create_all()


@app.route('/')
def index():
    details = Books.query.all()
    return render_template('index.html', details=details)
 
@app.route('/add', methods=['GET', 'POST'])
def add_books():
    if request.method == 'POST':
        book_title = request.form.get('title')
        book_author = request.form.get('author')
 
        add_detail = Books(
            title=book_title,
            author=book_author
        )
        db.session.add(add_detail)
        db.session.commit()
        return redirect(url_for('index'))
 
    return render_template('add_book.html')

@app.route('/delete/<int:id>')
def delete(id):
    # Deletes the data on the basis of unique id 
    # Redirects to home page
    data = Books.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    create_db()
    app.run(debug=True)

