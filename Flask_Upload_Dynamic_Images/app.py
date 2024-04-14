# app.py
# Flask Upload Dynamic Images

from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
import os
 
app = Flask(__name__)
 
upload_folder = os.path.join('static', 'uploads')
 
app.config['UPLOAD'] = upload_folder
 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        return render_template('index.html', img=img)
    return render_template('index.html')
 
@app.route('/about/')
def about():
    return render_template('about.html')
 
if __name__ == '__main__':
    app.run(debug=True)

