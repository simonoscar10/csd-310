import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.4jiwl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
cluster =  MongoClient(url)
db = cluster["pytech"]
students = db["students"]

docs = students.find({})
for doc in docs:
    print(doc)

Adam = {"Student ID":1010, "First Name":"Adam", "Last Name":"Allover"}
students.insert_one(Adam).inserted_id
students.delete_one({"Student ID":1010})

moreDocs = students.find({})
for doc in moreDocs:
    print(doc)