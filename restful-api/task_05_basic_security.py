#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

users = {
      "user1": {"username": "user1", "password": "<hashed_password>", "role": "user"},
      "admin1": {"username": "admin1", "password": "<hashed_password>", "role": "admin"}
    }

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username  # El nombre de usuario se pasa a la función protegida
    return None

@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def basic_protected():
    usuario = request.json.get('username')
    password = request.json.get('password')
    
    if usuario in users:
        return jsonify({"Basic Auth: Access Granted"}), 200
    
@app.route("/login", methods=['POST'])
def loguear():
    usuario = request.json.get('username')
    password = request.json.get('password')
    
    if not usuario or not password:
        return jsonify({"error": "Faltan credenciales"}, 400)
    
    elif check_password_hash(users[usuario]['password'], password):
        return jsonify({"mensaje": "Autorizacion exitosa", "role": users[usuario]['role']}), 200
    
    else:
        return jsonify({"error": "Contraseña incorrecta"}, 401)
    
    if usuario not in users:
        return jsonify({"Usuario no logueado"})
    
    else:
        return jsonify({})
    
if __name__ == "__main__":
    app.run()