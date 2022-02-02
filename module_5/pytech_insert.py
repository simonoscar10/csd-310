import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.4jiwl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
cluster =  MongoClient(url)
db = cluster["pytech"]
students = db["students"]

Oscar = {"Student ID":1007, "First Name":"Oscar", "Last Name":"Simon"}
Joe = {"Student ID":1008, "First Name":"Joe", "Last Name":"Murphy"}
Gerry = {"Student ID":1009, "First Name":"Gerry", "Last Name":"Bluff"}
students.insert_one(Oscar).inserted_id
students.insert_one(Joe).inserted_id
students.insert_one(Gerry).inserted_id