import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'

names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + '@gmail.com'
	password = ''.join(random.choice(chars) for i in range(12))



	print ("Sending username and password : " + username,password)