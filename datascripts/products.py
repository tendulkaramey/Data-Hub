productnames=[
'Samsung-Galaxy-M04',
'realme-narzo-N55',
'OnePlus-Nord-CE',
'Nokia-G21',
'Samsung-Galaxy-M13'
'Samsung-Galaxy-M14'
'Samsung-Galaxy-M15',
'realme-narzo-50A',
'Nokia-C12',
'Nokia-C122',
'Nokia-C125',
'Redmi-12C',
'OnePlus-11',
'Tecno-Spark-9',
'Honor-MagicBook-14',
'ASUS-Vivobook-15',
'ASUS-Vivobook-14',
'Acer-Aspire-5',
'Dell-Inspiron-3511',
'ASUS-Vivobook-16X',
'Lenovo-IdeaPad',
'Apple-2020-MacBook-Air',
'Apple-2021-MacBook-Air',
'HP-Chromebook-11a',
'HP-Pavilion-14',
'Dell-Vostro-3420',
'HONOR-MagicBook-X14',
'Samsung-Galaxy-Book2'
'Lenovo-IdeaPad-Slim-3'
'Canon-EOS-1500D',
'Nikon-Z50',
'Nikon-D85',
'Apple-Watch-SE',
'Apple-Watch-Series-8',
'Samsung-Galaxy-Watch5',
'Lenovo-Tab-Yoga-11',
'Samsung-Galaxy-Tab-A8',
'Redmi-Pad',
'Lenovo-Tab-M10',
'Samsung-Galaxy-Tab-A7',
'Apple-2022-10.9-inch-iPad',
'Apple-2021-10.2-inch',
'Xiaomi-Pad-5',
'OnePlus-Pad-29.49cm',
'Lenovo-Calling-Tab-M8'
'Lenovo-M10'


]

product_data=[]

key=1

for i in productnames:
	product_data.append({'id':key,'name':i})
	key +=1

with open('productdata.txt','w') as f:
	f.write(f"{product_data}\n")