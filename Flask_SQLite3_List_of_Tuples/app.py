# app.py
# Python SQLite3 List of Tuples

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('jacksons.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    band_of_brothers = conn.execute("SELECT name, age, address, salary FROM brothers;").fetchall()
    conn.commit()
    conn.close()

    return render_template('index.html', band_of_brothers=band_of_brothers)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

