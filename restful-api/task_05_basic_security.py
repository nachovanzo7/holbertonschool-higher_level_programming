#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

#request: permite acceso a datos de la solicitud HTTP
#HTTPBasicAuth: permite implementar autenticacion de la solicitud HTTP
#generate_password_hash: genera un hash seguro a partir de una contraseña
#check_password_hash: verifica si la contraseña ingresada coincide con el hash guardado
#JWTManager: administra la config y manejo de JWT
#create_access_token: crea un token de acceso JWT para un usuario autenticado
#jwt_required: decorador que se usa para proteger rutas, requeriendo un token válido
#get_jwt_identity: obtiene identidad del usuario actual a partir del token JWT

app = Flask(__name__)

# Configuración de la clave secreta para JWT
app.config['JWT_SECRET_KEY'] = 'super-secret-key' 
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Usuarios con contraseñas hash generadas
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Verificación de la autenticación básica
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username  # El nombre de usuario se pasa a la función protegida
    return None

@auth.error_handler
def unauthorized():
    return "401 Unauthorized", 401

# Ruta protegida con autenticación básica
@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200

#Cuando no está autorizado devolver 401 Unauthorized (string)

# Login y generación de token JWT
@app.route("/login", methods=['POST'])
def loguear():
    usuario = request.json.get('username')
    password = request.json.get('password')

    if not usuario or not password:
        return jsonify({"error": "Faltan credenciales"}), 400

    user = users.get(usuario)
    if user and check_password_hash(user['password'], password):
        # Crear el token JWT con el usuario y su rol
        access_token = create_access_token(identity={"username": usuario, "role": user['role']})
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

# Ruta protegida con JWT
@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

# Ruta solo para administradores
@app.route("/admin-only", methods=['GET'])
@jwt_required()
def only_admin():
    current_user = get_jwt_identity()
    
    if current_user['role'] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted", 200

# Controladores de errores personalizados para JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return "401 Unauthorized", 401 

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_data):
    return "401 Unauthorized", 401 

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_data):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_data):
    return jsonify({"error": "Fresh token required"}), 401

# Corrección en la ejecución de la app
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=False)
