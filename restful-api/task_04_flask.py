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
    
@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.json["username"] #Guardo el nombre de usuario
    nombre= request.json["name"] #Guardo el nombre
    edad = request.json["age"] #Guardo la edad
    ciudad = request.json["city"] #Guardo la ciudad
    
    if not username or not isinstance(username, str):
        return jsonify({"error":"Username is required"}), 400
    
    users_list[username] = {
        "username": username,
        "name": nombre,
        "age": edad,
        "city": ciudad
    }
    
    mensaje = {
        "message": "User added", "user": users_list[username]
    }
    
    if username in users_list:
        return jsonify(mensaje), 201
    
if __name__ == "__main__": app.run(host='localhost', port='5000', debug=False)