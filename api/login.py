from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api
from werkzeug.security import generate_password_hash, check_password_hash

# In-memory data store for registered users (replace this with a database)
users = []

login_api = Blueprint("login_api", __name__, url_prefix="/api/login")
api = Api(login_api)

class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return make_response(jsonify(error='Username and password are required'), 400)

        if any(user['username'] == username for user in users):
            return make_response(jsonify(error='Username is already taken'), 409)

        hashed_password = generate_password_hash(password)
        users.append({'username': username, 'password': hashed_password})
        return make_response(jsonify(message='Registration successful'), 201)

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = next((user for user in users if user['username'] == username), None)

        if not user:
            return make_response(jsonify(error='User not found'), 400)

        if not check_password_hash(user['password'], password):
            return make_response(jsonify(error='Invalid password'), 409)

        return make_response(jsonify(message='Login successful'), 200)

# Add user-related resources to the blueprint
api.add_resource(UserRegistration, '/register')
api.add_resource(UserLogin, '/login')