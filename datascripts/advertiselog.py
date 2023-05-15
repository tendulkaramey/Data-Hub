from users import users
import random
from random import randrange
from datetime import timedelta,datetime

#TIMESTAMP USERID AGE GENDER REGION MEDIUM CAMPAIGN SOURCE CONVERSION



def random_date(start= datetime.now()-timedelta(days=120), end=datetime.now()):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return str(start + timedelta(seconds=random_second))

utm_medium = [
	'SOCIAL','ORGANIC','EMAIL','PAID','AFFILIATES'
]

utm_campaign = [
	'DIWALI-SALE','FEATURE-LAUNCH','NEW-PRODUCTS','IPL22','IPL23-MUMBAI','T20WCP','IPL23-DELHI','IPL23-BLR'
]

utm_source = [
	'GOOGLE','INSTAGRAM','LINKEDIN','FACEBOOK','YAHOO','YOUTUBE','APP','BING','WHATSAPP'
]

logs = []
userlength = len(users)-1
mediumlength = len(utm_medium)-1
campaignlength = len(utm_campaign)-1
sourcelength = len(utm_source)-1

for i in range(0,500000):
    randomuser=users[random.randint(0,userlength)]
    randommedium=utm_medium[random.randint(0,mediumlength)]
    randomcampaign=utm_campaign[random.randint(0,campaignlength)]
    randomsource=utm_source[random.randint(0,sourcelength)]
    conversion=random.randint(0,1)
    conversion='YES' if conversion==1 else 'NO'

    logrow='{0} {1} {2} {3} {4} {5} {6} {7} {8} '.format(random_date(),randomuser['id'],randomuser['age'],randomuser['gender'],randomuser['region'],randommedium,randomcampaign,randomsource,conversion)
    logs.append(logrow)

with open('advertise.log', 'w') as f:
    for line in logs:
        f.write(f"{line}\n")