from flask import Flask, redirect, url_for, flash, render_template
from pymongo import MongoClient
import app

mongo_uri = "mongodb+srv://Cluster42678:dUVva0d3dVNY@cluster42678.dl8zutk.mongodb.net"
client = MongoClient(mongo_uri)
db = client['userData']
userRecords = db['userRecords']


def main():
    return 

def check_exists(query):
    count = userRecords.count_documents(query)
    return count > 0

def create_user(username, password):
    if check_exists({"username": username}):
        flash('Username is taken. Either sign in or try another username')
        return render_template('new_user.html')
    #User does not exist, create one and sign on
    result = userRecords.insert_one(
        {
            "username": username,
            "password": password
        }
    )
    return redirect(url_for('user_page', userN = username))   

def sign_in(username, password):
    if check_exists({"username":username, "password": password}):
        return redirect(url_for('user_page', userN = username))   
    flash('incorrect username or password, please try again')
    return render_template('sign_in.html')



if __name__ == "__main__":
    main()