#!/usr/bin/python3

from urllib import request
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users_list = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, 
              "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}


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
    username = request.json["username"] #Guardo el nombre de usuario
    nombre= request.json["name"] #Guardo el nombre de usuario
    edad = request.json["age"] #Guardo el nombre de usuario
    ciudad = request.json["city"] #Guardo el nombre de usuario
    
    if not username:
        return jsonify({"error":"Username is required"})
    
    if username in users_list:
        return jsonify("Usuario existente"), 400
    
    users_list[username] = {
        "username": username,
        "name": nombre,
        "age": edad,
        "city": ciudad
    }
    
    if username in users_list:
        return jsonify({"message": "User added", "user": users_list[username]}), 201
    
if __name__ == "__main__": app.run(host='localhost', port='8000', debug=False)