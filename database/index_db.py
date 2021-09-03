
import json
from pymongo import MongoClient 
  
  

myclient = MongoClient("mongodb://localhost:27017/") 
   
 
db = myclient["company_index"]
   

Collection = db["data"]

with open('company_index.json') as file:
    file_data = json.load(file)
      

if isinstance(file_data, list):
    Collection.insert_many(file_data)  
else:
    Collection.insert_one(file_data)