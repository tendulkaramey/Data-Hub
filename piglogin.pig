%default TODAYS_DATE `date +%Y-%m-%d`;
product = LOAD '/home/hadoop/hivedjango/product.log' USING PigStorage(' ') as (LOGLEVEL: chararray, DATE: chararray, TIMESTAMP: chararray, USERID: chararray, AGE: chararray, GENDER: chararray, REGION: chararray, OPERATION: chararray, PRODUCTID: chararray, PRODUCTNAME: chararray, ORDERID: chararray, PAYMENTMETHOD: chararray, COUPONNAME: chararray);

linlout = FILTER product BY OPERATION == 'LOGOUT' OR OPERATION == 'LOGIN';
filtered_linlout = FOREACH linlout GENERATE USERID, OPERATION, DATE, TIMESTAMP;
DUMP filtered_linlout;
store filtered_linlout into '/home/hadoop/hivedjango/pigoutputs/$TODAYS_DATE' using PigStorage(' ');