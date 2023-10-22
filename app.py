from flask import Flask, render_template, url_for, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('googleTest.html')
@app.route('/hello')
def form():
    return render_template('form.html')

def submit():
    address = request.form.get('address')
    return f"You submitted the address: {address}"

if __name__ == '__main__':
    app.run(debug=True)