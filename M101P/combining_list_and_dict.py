person = {'name': 'Fernando Morelli ', 'favorite_color': 'blue', 'hair': 'brown',
          'interests': ['cycling', 'running', 'golf']}

for key in person:
    if(key == 'interests'):
        print 'Interests....'
        for interests in person[key]:
            print '\tinterests is ' + interests
    else:
        print 'key is ' + key + ' value is ' + person[key] 