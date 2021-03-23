import sys
sys.path.append("../")

from helpers.mongoConnection import *
from bson import json_util
from flask import request

app = Flask("Celebrities's API")

@app.route("/")
def welcome():
    print("Welcome to Celebrities's API")
    return None

@app.route("/celebrities")
def get_celebrities():
    celeb = query_celebrity()
    return celeb

@app.route("/celebrities/details/<_id>")
def details(_id):
    _id = ObjectId(_id)
    resp = client.LabApi.Celebrities.find({"_id":_id})
    return list(resp)
