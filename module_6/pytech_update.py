import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.4jiwl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
cluster =  MongoClient(url)
db = cluster["pytech"]
students = db["students"]

docs = students.find({})
for doc in docs:
    print(doc)

students.update_one({"Student ID": 1007}, {"$set": {"Last Name":"Imagine"}})
students.find_one({"Student ID": 1007})