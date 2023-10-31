from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from model.playerz import Player
from model.playerz import CookieClicker
from model.playerz import BinaryGame
from model.playerz import GuessGame

player_api = Blueprint('player_api', __name__,
                   url_prefix='/api/players')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(player_api)

def cookieclicker_obj_by_username(username):
    """finds User in table matching username """
    id = Player.query.filter_by(_username=username).first().id
    return CookieClicker.query.filter_by(id=id).first()

def binarygame_obj_by_username(username):
    """finds User in table matching username """
    id = Player.query.filter_by(_username=username).first().id
    return BinaryGame.query.filter_by(id=id).first()

def guessgame_obj_by_username(username):
    """finds User in table matching username """
    id = Player.query.filter_by(_username=username).first().id
    return GuessGame.query.filter_by(id=id).first()

def findId(username): 
    id = Player.query.filter_by(_username=username).first().id
    return id 

def findPlayer(username): 
    player = Player.query.filter_by(_username=username).first()
    return player

class PlayerAPI:
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            username = body.get('username')
            if username is None or len(username) < 2:
                return {'message': f'Username is missing, or is less than 2 characters'}, 210
            
            po = Player(username=username)

            player = po.create()
            #Sucess returns json of user
            if player:
                return jsonify(player.read())
            #Failure returns error
            return {'message': f'Processed {username}, either a format error or duplicate'}, 210
    
    class _Authenticate(Resource):                  # Authenticates an user by checking the backend
        def post(self):
            body = request.get_json()               # grab info from frontend
            username = body.get('username')
            if len(username) < 1:
                return {'message': f'Invalid username'}, 210

    class _Read(Resource):
        def get(self):
            players = Player.query.all()    # read/extract all users from database
            json_ready = [player.read() for player in players]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
    
    class _ScoreCookie(Resource):
        def get(self):
            players = Player.query.all()
            cscore = [Player.cScore for player in players]
            return jsonify(cscore)
    
    class _HighScoreCookie(Resource):
        def get(self):
            players = Player.query.all()
            chighscore = max(Player.cScore for player in players if player.cScore is not None)
            return chighscore
    
    class _DeleteCookie(Resource):                     # This resource aims to delete a gpa row in the db
        def delete(self):
            body = request.get_json()               # We grab our body
            username = body.get('username')         # Get the username of the user from the cookie, will process in frontend
            player = cookieclicker_obj_by_username(username)
            if player:                                # Check if user exists
                player.delete()                       # call delete
            else:                                   # if user does not exist
                return {'message': f"unable to find GPA entries of user '{username}'"}, 210
            return player.read()
    
    class _UpdateCookie(Resource):
        def post(self):
            body = request.get_json()
            username = body.get(username)
            ccScore = int(body.get('cScore'))
            cCost = int(body.get('cCost'))
            cCount = int(body.get('cCount'))
            dbCost = int(body.get('dbCost'))
            dbCount = int(body.get('dbCount'))
            pCount = int(body.get('pCount'))
            rCost = int(body.get('rCost'))
            rate = int(body.get('rate'))

            player = cookieclicker_obj_by_username(username)
            if player:
                player.update(ccScore, cCost, cCount, dbCost, dbCount, pCount, rCost, rate)
            else:
                return {'message': f"unable to find Cookie Clicker entries of user '{username}'"}, 210     # error msg
            return player.read()
    
    class _ScoreBiinary(Resource):
        def get(self):
            players = Player.query.all()
            cscore = [Player.bScore for player in players]
            return jsonify(cscore)
    
    class _HighScoreBinary(Resource):
        def get(self):
            players = Player.query.all()
            bhighscore = max(Player.bScore for player in players if player.bScore is not None)
            return bhighscore
    
    class _DeleteBinary(Resource):                     # This resource aims to delete a gpa row in the db
        def delete(self):
            body = request.get_json()               # We grab our body
            username = body.get('username')         # Get the username of the user from the cookie, will process in frontend
            player = binarygame_obj_by_username(username)
            if player:                                # Check if user exists
                player.delete()                       # call delete
            else:                                   # if user does not exist
                return {'message': f"unable to find Binary Game entries of user '{username}'"}, 210
            return player.read()
    
    class _UpdateBinary(Resource):
        def post(self):
            body = request.get_json()
            username = body.get(username)
            bScore = int(body.get('bScore'))

            player = binarygame_obj_by_username(username)
            if player:
                player.update(bScore)
            else:
                return {'message': f"unable to find Binary Game entries of user '{username}'"}, 210     # error msg
            return player.read()
    
    class _ScoreGuess(Resource):
        def get(self):
            players = Player.query.all()
            cscore = [Player.gScore for player in players]
            return jsonify(cscore)
    
    class _HighScoreGuess(Resource):
        def get(self):
            players = Player.query.all()
            ghighscore = max(Player.gScore for player in players if player.gScore is not None)
            return ghighscore
    
    class _DeleteGuess(Resource):                     # This resource aims to delete a gpa row in the db
        def delete(self):
            body = request.get_json()               # We grab our body
            username = body.get('username')         # Get the username of the user from the cookie, will process in frontend
            player = guessgame_obj_by_username(username)
            if player:                                # Check if user exists
                player.delete()                       # call delete
            else:                                   # if user does not exist
                return {'message': f"unable to find Guess Game entries of user '{username}'"}, 210
            return player.read()
    
    class _UpdateGuess(Resource):
        def post(self):
            body = request.get_json()
            username = body.get(username)
            gScore = int(body.get('gScore'))

            player = guessgame_obj_by_username(username)
            if player:
                player.update(gScore)
            else:
                return {'message': f"unable to find Guess Game entries of user '{username}'"}, 210     # error msg
            return player.read()





"""from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building

from model.players import Player

# Change variable name and API name and prefix
player_api = Blueprint('player_api', __name__,
                   url_prefix='/api/players')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(player_api)

class PlayerAPI:     
    class Action(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            name = body.get('name')
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210
            # validate uid
            uid = body.get('uid')
            if uid is None or len(uid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            # look for password and tokens
            password = body.get('password')
            tokens = body.get('tokens')

            ''' #1: Key code block, setup PLAYER OBJECT '''
            po = Player(name=name, 
                        uid=uid,
                        tokens=tokens)
            
            ''' Additional garbage error checking '''
            # set password if provided
            if password is not None:
                po.set_password(password)            
            
            ''' #2: Key Code block to add user to database '''
            # create player in database
            player = po.create()
            # success returns json of player
            if player:
                return jsonify(player.read())
            # failure returns error
            return {'message': f'Processed {name}, either a format error or User ID {uid} is duplicate'}, 210

        def get(self):
            players = Player.query.all()    # read/extract all players from database
            json_ready = [player.read() for player in players]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

        def put(self):
            body = request.get_json() # get the body of the request
            uid = body.get('uid') # get the UID (Know what to reference)
            data = body.get('data')
            player = Player.query.get(uid) # get the player (using the uid in this case)
            player.update(data)
            return f"{player.read()} Updated"

        def delete(self):
            body = request.get_json()
            uid = body.get('uid')
            player = Player.query.get(uid)
            player.delete()
            return f"{player.read()} Has been deleted"


    # building RESTapi endpoint, method distinguishes action
    api.add_resource(Action, '/')
    """
