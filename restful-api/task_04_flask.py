#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users_list = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users_list.keys()))

@app.route("/status")
def status():
    return ("OK")

@app.route("/users/<username>", methods=['GET'])
def user(username):
    if username in users_list:
        return jsonify(users_list[username]), 200
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route('/add_users', methods=['POST'])
def add_user():
    user = request.get_json()
    username = user.get('username') #Guardo el nombre de usuario
    nombre = user['name']
    edad = user['age'] #Guardo el nombre de usuario
    ciudad = user['city'] #Guardo el nombre de usuario
    
    if not username or not isinstance(username, str):
        return jsonify({"error":"Username is required"}), 400

    users_list['username'] = {
        "city": ciudad,
        "age": edad,
        "name": nombre,
        "username": username
    }
    
    if username in users_list:
        return jsonify({"message": "User added", "user": users_list[username]}), 201
    
if __name__ == "__main__": app.run(host='localhost', port='5000', debug=False)