from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

score_api = Blueprint("score_api", __name__, url_prefix="/api/scores")
api = Api(score_api)

# In-memory data store for game scores
game_scores = []

# Dictionary to store user-specific data
user_data = {}

class ScoreAPI(Resource):
    def get(self):
        return jsonify()

    def post(self):
        data = request.get_json()
        score = data.get('score')

        if score is not None and isinstance(score, int):
            game_scores.append(score)
            return jsonify(message='Score stored successfully'), 201
        else:
            return jsonify(error='Invalid score format'), 400

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
        return jsonify(message='User data stored successfully'), 201


api.add_resource(UserDataAPI, '/users/<string:user_id>/')
