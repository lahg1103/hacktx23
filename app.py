from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def airplanes():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)