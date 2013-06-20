
import bottle
import pymongo

# this is the handler for the default path of the web server

@bottle.route('/')
def home_page():
  mythings = [ 'apple', 'orange', 'banana', 'peach' ]
  # return bottle.template('hello_world', username='Michael', things=mythings)
  return bottle.template('hello_world', { 'username' :'Michael', 'things' : mythings} )

@bottle.route('/testpage')
def testpage():
  return "This is a test page."

bottle.debug(True)
bottle.run(host='localhost', port=8080)
