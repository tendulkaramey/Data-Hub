from pyhive import hive
conn = hive.Connection(host='localhost',port=10000,database='hiveyagodb',username='hive')
cursor = conn.cursor()



#cursor.execute("select distinct object from datastore where predicate='<hasGivenName>' and subject in (select subject from hiveyagodb.datastore where predicate='<livesIn>' group by subject having count(*) > 1)")
#print(cursor.fetchall())