import json
from pymongo import MongoClient
import os
import sys

fn = sys.argv[1]

connectionString = "mongodb://admin:admin@127.0.0.1:27017"
client = MongoClient(connectionString)
db=client.DBLP
publis=db.publis

# Loading or Opening the json file
with open(fn) as file:
	file_data = json.load(file)
	
# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else inser_one is used
if isinstance(file_data, list):
	publis.insert_many(file_data)
else:
	publis.insert_one(file_data)

nb_doc = publis.count_documents({})

print('======================\n')
print("il y a ", nb_doc, "document(s) dans la base\n") #15000 avant import
print('----------------------\n')
client.close()