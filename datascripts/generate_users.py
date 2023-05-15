import random_names
import random

users = []
userid=10001
first_names=[]
last_names=[]
genders=['M','F']
for i in range(0,50):
	first_name = random_names.First()
	last_name = random_names.Last()
	while first_name in first_names:
		first_name = random_names.First()
	while last_name in last_names:
		last_name = random_names.Last()
	users.append({
		'id':userid,'first_name':first_name,'last_name':last_name,'age':random.randint(18,70),'region':random_names.Places()
		,'gender':genders[random.randint(0,1)]})
	first_names.append(first_name)
	last_names.append(last_name)
	userid += 1

with open('userdatatest.txt', 'w') as f:
	f.write(f"{users}\n")