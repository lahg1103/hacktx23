from flask import Flask, render_template, url_for, request, jsonify
from pymongo import MongoClient


app = Flask(__name__)

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
    data = request.json['data']
    return jsonify({'data': data})


if __name__ == '__main__':
    app.run(debug=True)