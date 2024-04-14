# app.py
# Flask Upload Local Images


from flask import Flask, render_template
import os
 
app = Flask(__name__)
 
img = os.path.join('static', 'images')
 
@app.route('/')
def index():
    file = os.path.join(img, 'Geek_Python.png')
    return render_template('index.html', image=file)

@app.route('/about/')
def about():
    return render_template('about.html')
 
if __name__ == '__main__':
    app.run(debug=True)



