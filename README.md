#Steps:

1. - Generate data files from python scripts (as we did not found any good datasets for problem we were working on). We have used datasets with 5 lakhs records per file.
1. - Use pig scripts to process the data and extract important information in structured format and store it in txt files,upload the files to HDFS.
1. - Store the processed data in structured format in hive tables.
1. - Use hive queries to extract valuable insights from the data such as top 5 products purchased, distribution of payment methods etc.
1. - Store the hive queries data into mysql database.
1. - Connect django with mysql database to get the valuable insights and show analytics on user interface.
1. - Repeat the above steps periodically using cron job/scheduler


#Step 1:

Scripts to create data files are stored in datascripts folder.
names of py files are:
1. advertiselog.py
1. productlog.py
1. serverlog.py

you can create new log files by tunning the script or use the already created files from datascript folder.
names of log files are:
1. advertise.log
1. server.log
1. product.log

#Step 2:
set the load path of data files in pigscripts based on your file systems and run the scripts, output will be stored in pigoutputs folder.
names of pig scripts are:
1. pigproduct.pig
1. advertise.pig
1. serverlogs.pig

and then upload the pig output files to hdfs into:
1. /ecommercedata/logindata/
1. /ecommercedata/cartdata/
1. /ecommercedata/purchasedata/
1. /ecommercedata/pviewdata/
1. /ecommercedata/advertisedata/
1. /ecommercedata/serverdata/

based on how many files pig generates, you need to add those many to hdfs.

#Step 3:

now first run the initialisehive.hiveql which will create database and table into your system.
then run hiveinsert.hiveql which will insert pig output data to hive tables.

