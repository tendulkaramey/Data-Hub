import random 
from users import users
from random import randrange
from datetime import timedelta,datetime

#LEVEL TIMESTAMP METHOD API STATUS USERID

def random_date(start= datetime.now()-timedelta(days=120), end=datetime.now()):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return str(start + timedelta(seconds=random_second))

api_list = [
	'/api/cart','/api/order','/api/products/{0}/coupons','/api/users/profile','/api/login','/api/logout'
]

status_codes = [
	500,200,202,400,404,301,308,401,403,405,408,409,502
]

method = ['GET', 'POST', 'DELETE','PUT']

statuscodelength = len(status_codes) - 1
apilistlength = len(api_list) - 1
userslength = len(users) - 1
methodlength=len(method) - 1

logs = []

for i in range(0,500000):
	randomuser=users[random.randint(0,userslength)]
	randomstatus=status_codes[random.randint(0,statuscodelength)]
	randomapi=api_list[random.randint(0,apilistlength)]
	randommethod=method[random.randint(0,methodlength)]
	if randomapi == '/api/products/{0}/coupons':
		randomapi = '/api/products/{0}/coupons'.format(random.randint(1000,200000))
	if randomstatus in [200,202]:
		randomloglevel='INFO'
	elif randomstatus in [400,404,301,308,401,403,405,408,409]:
		randomloglevel='WARNING'
	else:
		randomloglevel='ERROR'
	logrow='{0} {1} {2} {3} {4} {5}'.format(randomloglevel,random_date(),randommethod,randomapi,randomstatus,randomuser['id'])
	logs.append(logrow)

with open('server.log', 'w') as f:
    for line in logs:
        f.write(f"{line}\n")