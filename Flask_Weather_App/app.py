# app.py
# Flask Weather App

# import the Flask web framework
from flask import Flask,render_template,request,abort

# import json to load json data to python dictionary
import json

# urllib.request to make a request to api
import urllib.request

# create an instance of the Flask class for our web app
app = Flask(__name__)

def tocelcius(temp):
    return str(round(float(temp) - 273.16,2))

def tofahrenheit(temp):
    return str(round(float(temp - 273.16) * (9/5) + 32,2))

@app.route('/',methods=['POST','GET'])
def weather():
    api_key = '183ba3fa699e945bc943327c1c88b4ff'
    if request.method == 'POST':
        city = request.form['city']
    else:
        #for default name Blackfoot
        city = 'Blackfoot'

    # source contain json data from api
    try:
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid='+api_key).read()
    except:
        return abort(404)
    # converting json data to dictionary
    list_of_data = json.loads(source)

    # data for variable list_of_data
    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'k',
        "temp_cel": tocelcius(list_of_data['main']['temp']) + 'C',
        "temp_fahr": tofahrenheit(list_of_data['main']['temp']) + 'F',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
        "cityname":str(city),
    }
    return render_template('index.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)
