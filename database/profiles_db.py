
import json
from pymongo import MongoClient 
  
  

myclient = MongoClient("mongodb://localhost:27017/") 
 
db = myclient["company_profile"]
   

Collection = db["data"]
  

with open('company_profiles.json') as file:
    file_data = json.load(file)
      

if isinstance(file_data, list):
    Collection.insert_many(file_data)  
else:
    Collection.insert_one(file_data)