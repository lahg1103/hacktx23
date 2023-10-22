from flask import Flask, render_template, url_for, request, jsonify
from pymongo import MongoClient
from python.airport_search import AirportSearch
from python.flight_search import FlightSearch
from python.flight_data import FlightData
from python.google_api import GoogleSearch

import user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'theSecretKey'

googleSearch = GoogleSearch()
airportSearch = AirportSearch()
flightSearch = FlightSearch()

mongo_uri = "mongodb+srv://Cluster42678:dUVva0d3dVNY@cluster42678.dl8zutk.mongodb.net"
client = MongoClient(mongo_uri)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('googleTest.html')
@app.route('/hello')
def form():
    return render_template('form.html')

def submit():
    address = request.form.get('address')
    return f"You submitted the address: {address}"


@app.route('/process_long_lat', methods=['POST'])
def process_long_lat():
    dataLat = request.json['data'][0]
    dataLng = request.json['data'][1]

    user_city, user_lat, user_lng = airportSearch.user_location()
    from_iata, from_city, from_country = airportSearch.search(user_lat, user_lng)
    iata, cities, countries = airportSearch.search(dataLat, dataLng)
    

    for fi in from_iata:
        for ti in iata: 
            result = flightSearch.search(fi, ti) 
            if "_results" in result:
                if len(result["data"]) > 0:
                    op = result["data"][0]["route"][0]["operating_carrier"]
                    flight = result["data"][0]["route"][0]["operating_flight_no"]

                    data = googleSearch.search(fi, ti, op, flight)
                    print (result)

                    break

    return jsonify({'cities': cities, 'countries': countries}) 

#pass in the dates 
@app.route('/process_from_to_dates', methods=['POST'])
def from_to_dates():
    from_date = request.form['from']
    to_date = request.form['to']


    return #render_template('googleTest.html') 

#Pass in user id to authenticate and locate user, post?
@app.route('/user/<userN>')
def user_page(userN):
    return render_template('user.html', username = userN)

@app.route('/user/create-user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return user.create_user(username=  username, password= password)
    return render_template('new_user.html')

@app.route('/user/sign-in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return user.sign_in(username=  username, password= password)
    return render_template('sign_in.html')    

if __name__ == '__main__':
    app.run(debug=True)