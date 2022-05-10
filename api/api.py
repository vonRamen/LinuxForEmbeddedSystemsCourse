from bottle import route, run, template, request
import paho.mqtt.client as mqtt
from pymongo import MongoClient
import time    
import json
from bson.json_util import dumps

client = MongoClient('localhost', 27017)
db = client["data"]


@route('/<data>')
def index(data):
    time_from = int(request.query['from'])
    time_to = int(request.query['to'])
    col = db["smart_alarm/data/"+data]

    return dumps(col.find({"timestamp": {"$gt": time_from, "$lte": time_to}}))

run(host='localhost', port=8080)