#!/usr/bin/python3

from urllib import request
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users_list = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
         "Laura": {"name": "Laura", "age": 22, "city": "Los Angeles"},
         "Pepe": {"name": "Pepe", "age": 31, "city": "Los Angeles"},
         "Graciela": {"name": "Graciela", "age": 20, "city": "Los Angeles"}}


@app.route("/")
def home():
    return "Bienvenido a la API de Flask!"

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
        return jsonify("User not found"), 404
    

    
@app.route("/add_user", methods=['POST'])
def add_user():
    usuario_nuevo = request.get_json() #Pido los datos
    username = usuario_nuevo["username"] #Guardo el nombre de usuario
    
    if not username:
        return jsonify({"error": "Username requerido"})
    
    if username in users_list:
        return jsonify("Usuario existente"), 400
    
    users_list[username] = {
        "name": usuario_nuevo["name"],
        "age": usuario_nuevo["age"],
        "city": usuario_nuevo["city"]
    }
    
    return jsonify("Usuario creado con exito papaaaa")
    
if __name__ == "__main__": app.run(host='localhost', port='8000', debug=False)