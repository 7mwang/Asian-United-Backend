import sqlite3
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api
from werkzeug.security import generate_password_hash, check_password_hash
import os
# Get the absolute path to the 'instance' directory
instance_directory = os.path.abspath('instance')

# Specify the absolute path to the database file
db_file_path = os.path.join(instance_directory, 'volumes', 'scores.db')
print(db_file_path)
# Connect to the database using the absolute path
login_api = Blueprint("login_api", __name__, url_prefix="/api/login")
api = Api(login_api)

# ...

class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return make_response(jsonify(error='Username and password are required'), 400)

        # Connect to the database
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()

        # Check if the username is already taken
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            return make_response(jsonify(error='Username is already taken'), 409)

        hashed_password = generate_password_hash(password)
        cursor.execute('''INSERT INTO users (username, password) VALUES(?, ?)''', (username, hashed_password))
        conn.commit()
        conn.close()

        return make_response(jsonify(message='Registration successful'), 201)

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Connect to the database
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        if not user:
            return make_response(jsonify(error='User not found'), 400)

        if not check_password_hash(user[2], password):
            return make_response(jsonify(error='Invalid password'), 409)

        return make_response(jsonify(message='Login successful'), 200)

# ...

# Add user-related resources to the blueprint
api.add_resource(UserRegistration, '/register')
api.add_resource(UserLogin, '/login')
