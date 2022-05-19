from bottle import route, run, template, request, post, get, HTTPResponse
import paho.mqtt.client as mqtt
from pymongo import MongoClient
import time    
import json
from bson.json_util import dumps

#client = MongoClient('192.168.10.193', 27017)
client = MongoClient('localhost', 27017)
db = client["data"]

allowedDataCollections = ["temperature", "co2", "humidity"]


@get('/<data>')
def getData(data):
    time_from = int(request.query['from'])
    time_to = int(request.query['to'])
    col = db["smart_alarm/data/"+data]

    return dumps(col.find({"timestamp": {"$gt": time_from, "$lte": time_to}}))


@post('/<data>')
def postData(data):
    if data in allowedDataCollections:
        payload = json.load(request.body)
        
        col = db["smart_alarm/data/"+data]
        x = col.insert_one(payload)
    else:
        return HTTPResponse(status=400, body="Only temperature, co2 and humidity are allowed routes!")

run(host='localhost', port=8080)