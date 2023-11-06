from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
import sqlite3
import os
# Get the absolute path to the 'instance' directory
instance_directory = os.path.abspath('instance')

# Specify the absolute path to the database file
db_file_path = os.path.join(instance_directory, 'volumes', 'scores.db')

# Connect to the database using the absolute path
score_api = Blueprint("score_api", __name__, url_prefix="/api/scores")
api = Api(score_api)

# In-memory data store for game scores
game_scores = []

# Dictionary to store user-specific data
user_data = {}

class ScoreAPI(Resource):
    class ScoreAPI(Resource):
        def post(self):
            data = request.get_json()
            username = data.get('username')
            new_score = data.get('score')

            # Connect to the database
            conn = sqlite3.connect(db_file_path)
            cursor = conn.cursor()

            # Check if the user already exists in the database
            cursor.execute('SELECT * FROM game_scores WHERE username = ?', (username,))
            user = cursor.fetchone()

            if user:
                # If the user exists, update their score
                cursor.execute('UPDATE game_scores SET score = ? WHERE username = ?', (new_score, username))
            else:
                # If the user doesn't exist, create a new user entry
                cursor.execute('INSERT INTO game_scores (username, score) VALUES (?, ?)', (username, new_score))

            # Commit changes and close the database connection
            conn.commit()
            conn.close()

            return make_response(jsonify(message='Score updated successfully'), 200)
    def get(self):
        # Connect to the database
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()

        # Retrieve the top 10 scores from the database
        cursor.execute('SELECT username, score FROM game_scores ORDER BY score DESC LIMIT 10')
        top_10_scores = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Create a list of dictionaries from the fetched data
        top_scores_data = [{'username': row[0], 'score': row[1]} for row in top_10_scores]

        return make_response(jsonify(top_scores_data), 200)
api.add_resource(ScoreAPI, '/')

class UserDataAPI(Resource):
    def get(self, user_id):
        # Connect to the database
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()

        # Retrieve the user data for the specified user_id
        cursor.execute('SELECT * FROM user_data WHERE user_id = ?', (user_id,))
        data = cursor.fetchone()

        if data:
            user_data = {
                'count': data[1],
                'rate': data[2],
                'cost': data[3],
                'clickerCost': data[4],
                'clickerCount': data[5],
                'doubleCount': data[6],
                'dbCost': data[7],
                'plusCount': data[8],
            }
        else:
            user_data = {
                'count': 0,
                'rate': 1,
                'cost': 100,
                'clickerCost': 1000,
                'clickerCount': 0,
                'doubleCount': 0,
                'dbCost': 1500,
                'plusCount': 0,
            }

        # Close the database connection
        conn.close()

        return jsonify(user_data)

    def post(self, user_id):
        data = request.get_json()

        # Connect to the database
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()

        cursor.execute('INSERT OR REPLACE INTO user_data (user_id, count, rate, cost, clickerCost, clickerCount, doubleCount, dbCost, plusCount) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (user_id, data.get('count', 0), data.get('rate', 1), data.get('cost', 100), data.get('clickerCost', 1000), data.get('clickerCount', 0), data.get('doubleCount', 0), data.get('dbCost', 1500), data.get('plusCount', 0)))

        # Commit changes and close the database connection
        conn.commit()
        conn.close()

        return make_response(jsonify(message='User data stored successfully'), 201)

api.add_resource(UserDataAPI, '/users/<string:user_id>/')
