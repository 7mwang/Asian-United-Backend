from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model.jokes import *

joke_api = Blueprint('joke_api', __name__,
                   url_prefix='/api/jokes')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(joke_api)

class JokesAPI:
    # getRandomJoke()
    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomJoke())
    
    # getRandomJoke()
    class _ReadCount(Resource):
        def get(self):
            count = countJokes()
            countMsg = {'count': count}
            return jsonify(countMsg)


    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_ReadRandom, '/random')
    api.add_resource(_ReadCount, '/count')
    
if __name__ == "__main__": 
    #server = "http://127.0.0.1:8640" # run local
    server = 'https://asianunited.stu.nighthawkcodingsociety.com' # run from web
    url = server + "/api/jokes"
    responses = []  # responses list

    # get count of jokes on server
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    # update likes/dislikes test sequence
    num = str(random.randint(0, count-1)) # test a random record
    responses.append(
        requests.get(url+"/"+num)  # read joke by id
    )
    responses.append(
        requests.get(url+"/random")  # read a random joke
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")