import pymysql
import json 
import csv
from datetime import datetime
def mysqlconnect():
	# To connect MySQL database
	conn = pymysql.connect(
		host='localhost',
		user='root',
		password = '',
		db='nosqlproject',
        port=3307
		)
	product_stats = {}
	stats_order = ['product_purchased','product_clicks','added_in_cart','removed_from_cart','distinct_regions','coupons_used']
	
	with open('hiveoutputs/p1.txt', 'r') as f:
		reader = csv.reader(f, dialect='excel', delimiter='\t')
		start = 0
		for row in reader:
			product_stats[stats_order[start]] = row[0]
			start += 1
	plabels = []
	pdata = []
	with open('hiveoutputs/p2.txt', 'r') as f:
		reader = csv.reader(f, dialect='excel', delimiter='\t')
		start = 0
		for row in reader:
			plabels.append(row[0])
			pdata.append(int(row[1]))
		plabels = ','.join(plabels)
		pdata = str(pdata)

	with open('hiveoutputs/p4.txt', 'r') as f:
		reader = csv.reader(f, dialect='excel', delimiter='\t')
		logincount = 0
		logoutcount = 0
		ld = []
		for row in reader:
			ld.append(int(row[0]))
		lc = sum(ld)
		loginp = round((ld[0]/lc),2)*100
		logoutp = round((ld[1]/lc),2)*100
		newls = str([loginp,logoutp])

	rlabels = []
	rdata = []
	with open('hiveoutputs/p3.txt', 'r') as f:
		reader = csv.reader(f, dialect='excel', delimiter='\t')
		for row in reader:
			rlabels.append(row[0])
			rdata.append(int(row[1]))
		rsum = sum(rdata)
		rdata = [round((i/rsum),2)*100 for i in rdata]
		rlabels = ','.join(rlabels)
		rdata = str(rdata)

	pylabels = []
	pydata = []
	with open('hiveoutputs/p5.txt', 'r') as f:
		reader = csv.reader(f, dialect='excel', delimiter='\t')
		for row in reader:
			pylabels.append(row[0])
			pydata.append(int(row[1]))
		pysum = sum(pydata)
		pydata = [round((i/pysum),2)*100 for i in pydata]
		pylabels = ','.join(pylabels)
		pydata = str(pydata)
	
	cur = conn.cursor()
	datareq = {
      "data":{
        "stats":product_stats,
        "top_products":{
          "labels":plabels,
          "data":pdata
        },
        "loginlogout":{
          "labels":"Login,Logout",
          "data":newls
        },
        "payments":{
          "labels":pylabels,
          "data":pydata
        },
        "regions":{
          "labels":rlabels,
          "data":rdata
        }
      }
    }

	with open('hiveoutputs/s1.txt', 'r') as f:
		reader = csv.reader(f, dialect='excel', delimiter='\t')
		s1data = []
		for row in reader:
			s1data.append(int(row[0]))

	s2labels = []
	s2data = []
	with open('hiveoutputs/s2.txt', 'r') as f:
		reader = csv.reader(f, dialect='excel', delimiter='\t')
		for row in reader:
			s2labels.append(row[0])
			s2data.append(int(row[1]))
		s2labels = ','.join(s2labels)
		s2data = str(s2data)

	s3labels = []
	s3data = []
	with open('hiveoutputs/s3.txt', 'r') as f:
		reader = csv.reader(f, dialect='excel', delimiter='\t')
		for row in reader:
			s3labels.append(row[0])
			s3data.append(int(row[1]))
		s3labels = ','.join(s3labels)
		s3data = str(s3data)

	sdata =   {
	"data": {
		"stats": {
		"api_served": str(s1data[0]),
		"api_failed": str(s1data[1]),
		"users": str(s1data[2]),
		},
		"top_apis": {
		"labels": s2labels,
		"data": s2data
		},
		"api_status": {
		"labels": s3labels,
		"data": s3data
		}
	}
	}
	with open('hiveoutputs/a1.txt', 'r') as f:
		reader = csv.reader(f, dialect='excel', delimiter='\t')
		a1data = []
		for row in reader:
			a1data.append(int(row[0]))
		a1conv = str(round((a1data[1]/a1data[0]),2)*100)
	a2labels = []
	a2data = []
	with open('hiveoutputs/a2.txt', 'r') as f:
		reader = csv.reader(f, dialect='excel', delimiter='\t')
		for row in reader:
			a2labels.append(row[0])
			a2data.append(int(row[1]))
		a2labels = ','.join(a2labels)
		a2data = str(a2data)
	a3labels = []
	a3data = []
	with open('hiveoutputs/a3.txt', 'r') as f:
		reader = csv.reader(f, dialect='excel', delimiter='\t')
		for row in reader:
			a3labels.append(row[0])
			a3data.append(int(row[1]))
		a3labels = ','.join(a3labels)
		a3data = str(a3data)
	adata = {
	"data": {
	"stats": {
		"campaign_clicks": str(a1data[0]),
		"conversion": a1conv,
		"user_clicks": str(a1data[2]),
	},
	"campaign_clicks": {
		"labels": a2labels,
		"data": a2data
	},
	"source": {
		"labels": a3labels,
		"data": a3data
	}
	}
	}

	data = json.dumps(datareq)
	sdata = json.dumps(sdata)
	adata = json.dumps(adata)
	datetimes = str(datetime.now())
	sql = "INSERT INTO dashboard_dashboardstats (product_data,server_log_data,advertise_data,created_at) VALUES (%s, %s, %s, %s)"
	val = (data,sdata,adata,datetime.now())
	cur.execute(sql, val)
	#output = cur.fetchall()
	#print(output)
	conn.commit()
	
	# To close the connection
	conn.close()


# Driver Code
if __name__ == "__main__" :
	mysqlconnect()
