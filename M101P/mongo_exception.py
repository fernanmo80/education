import sys
import pymongo

def main():
  
  connection = pymongo.MongoClient("mongodb://localhost")

  db = connection.test
  users = db.users

  doc = {'firstname':'Andrew', 'lastname':'Erlichson'}
  print doc
  print "about to insert the document"

  try:
    users.insert(doc)
  except:
    print "insert failed", sys.exc_info()[0]

  print doc
  print "inserting again"

  doc = {'firstname':'Andrew', 'lastname':'Erlichson'}
 
  try:
    users.insert(doc)
  except:
    print "insert failed", sys.exc_info()[0]

main()



