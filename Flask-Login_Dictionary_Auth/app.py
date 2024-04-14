# app.py
# Flask-Login Example

from flask import Flask, request, render_template

app = Flask(__name__)

# add database like login credentials, username and password.
database = {'Big_Mike': 'foobar1',
			'BigMike': 'foobar2',
			'Mike': 'foobar3'}

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/login_form', methods=['POST', 'GET'])
def login():
	username = request.form['username']
	password = request.form['password']
	if username not in database:
		return render_template('index.html',
							info='Invalid User!')
	else:
		if database[username] != password:
			return render_template('index.html',
								info='Invalid Password!')
		else:
			return render_template('welcome.html', name=username)

@app.route('/about')
def about():
	return render_template('about.html')

# Run flask in debug mode
if __name__ == '__main__':
	app.run(debug=True)
	
