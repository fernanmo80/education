
import pymongo

from pymongo import MongoClient

# connect to database
connection = MongoClient('localhost',27017)

db = connection.test

# handle to names collection
names = db.names

# save in collection names
#db.names.save({'name':'Alonso'})


item = names.find_one()

print item['name']
