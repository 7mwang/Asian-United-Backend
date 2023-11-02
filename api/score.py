from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource

score_api = Blueprint("score_api", __name__, url_prefix="/api/scores")
api = Api(score_api)

# In-memory data store for game scores
game_scores = []

# Dictionary to store user-specific data
user_data = {}

class ScoreAPI(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        new_score = data.get('score')

        # Check if the user already exists in the data store
        user = next((user for user in game_scores if user['username'] == username), None)

        if user:
            # If the user exists, update their score
            user['score'] = new_score
            return make_response(jsonify(message='Score updated successfully'), 200)
        else:
            # If the user doesn't exist, create a new user entry
            game_scores.append({'username': username, 'score': new_score})
            return make_response(jsonify(message='New user created with score'), 201)
    def get(self):
        sorted_scores = sorted(game_scores, key=lambda x: x['score'], reverse=True)
        top_10_scores = sorted_scores[:10]
        return make_response(jsonify(top_10_scores), 201)
api.add_resource(ScoreAPI, '/')
class UserDataAPI(Resource):
    def get(self, user_id):
        if user_id in user_data:
            return jsonify(user_data[user_id])
        else:
            user_data[user_id] = {
            'count': 0,
            'rate': 1,
            'cost': 100,
            'clickerCost': 1000,
            'clickerCount': 0,
            'doubleCount': 0,
            'dbCost': 1500,
            'plusCount': 0,
            }
            return jsonify(user_data[user_id])

    def post(self, user_id):
        data = request.get_json()

        user_data[user_id] = {
            'count': data.get('count', 0),
            'rate': data.get('rate', 1),
            'cost': data.get('cost', 100),
            'clickerCost': data.get('clickerCost', 1000),
            'clickerCount': data.get('clickerCount', 0),
            'doubleCount': data.get('doubleCount', 0),
            'dbCost': data.get('dbCost', 1500),
            'plusCount': data.get('plusCount', 0),
        }
        return make_response(jsonify(message='User data stored successfully'), 201)


api.add_resource(UserDataAPI, '/users/<string:user_id>/')
