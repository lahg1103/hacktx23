from flask import Flask, render_template, url_for, request, jsonify
from pymongo import MongoClient
from python.airport_search import AirportSearch
import user
from bson import json_util
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'theSecretKey'

airportSearch = AirportSearch()
mongo_uri = "mongodb+srv://Cluster42678:dUVva0d3dVNY@cluster42678.dl8zutk.mongodb.net"
client = MongoClient(mongo_uri)
db = client['userData']
userRecords = db['userRecords']
flightRecords = db['flightRecords']

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

    airports, cities, countries = airportSearch.search(dataLat, dataLng)
    user_loc = airportSearch.user_location()



    return jsonify({'cities': cities, 'countries': countries}) 

#Pass in user id to authenticate and locate user, post?
@app.route('/user/<userN>')
def user_page(userN):
    return render_template('user.html', username = userN)

@app.route('/user/<userN>/flights')
def user_flights(userN):
    flights = flightRecords.find({"username": userN})
    return json.dumps(list(flights), default=json_util.default)


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