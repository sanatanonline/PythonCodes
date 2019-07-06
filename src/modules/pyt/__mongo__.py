import pymongo
from pymongo import MongoClient

mongo_client = MongoClient('localhost:27017',
                           username='genlogos',
                           password='genlogos',
                           authMechanism='SCRAM-SHA-1')

mongo_db = mongo_client["genlogos"]
mongo_col = mongo_db["customers"]

c_dict = {"name": "John", "address": "Highway 37"}

x = mongo_col.insert_one(c_dict)

print(x.inserted_id)

x = mongo_col.find_one()

my_query = {"address": "Highway 37"}

my_doc = mongo_col.find(my_query)

for x in my_doc:
    print(x)

print(x)
