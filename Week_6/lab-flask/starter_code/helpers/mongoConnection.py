from pymongo import MongoClient

client = MongoClient()

def query_celebrity(name={}):
    
    if name != {}:
        resp = client.LabApi.Celebrities.find({"name":name})
    else:
        resp = client.LabApi.Celebrities.find(name, {"_id":1, "name":1})
    
    return list(resp)

def insert_celebrity(collection, dic):
    return client.LabApi.Celebrities.insert_one(dic)
