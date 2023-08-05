from flask import Config, Flask, flash, jsonify, redirect, request
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
import yaml
from werkzeug.utils import secure_filename
import os
from utils import *
import subprocess
import os
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

client = MongoClient('mongodb://localhost:27017')
db = client['sales']
app = Flask(__name__)

CORS(app)
@app.route('/')
def hello_world():
    return "success"

@app.route('/users', methods=['POST', 'GET'])
def data():
    
    # POST a data to database
    if request.method == 'POST':
        body = request.json
        name = body['name']
        email = body['email']
        password = body['password'] 
        # db.users.insert_one({
        db['users'].insert_one({
            "name": name,
            "email": email,
            "password":password
        })
        return jsonify({
            'status': 'Data is posted to MongoDB!',
            'name': name,
            'email': email,
            'password':password
        })

@app.route('/upload', methods=['GET','POST'])
def upload():
        file=request.files['file'].read()
        c=request.form['c']
        per=request.form['per']
        print(c,per)
        f=open("sales.csv",'wb')
        f.write(file)
        f.close()
        p=subprocess.Popen("python ml.py "+per+" "+str(c),shell=True)
        p.wait()
        return "SUCCESS"       
            
    
if __name__ == "__main__":
    app.run(debug=True)
    