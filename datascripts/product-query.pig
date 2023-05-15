
/* 
	1.login-logout (id, userid, action(login/logout) timestamp)
	2.cart(id,userid,age,region,productid,product name,timestamp,action(add/remove))
	3.purchase(id,userid,age,region,productid,product name, timestamp, orderid, coupon name, payment method)
	4.product-view(id,userid,age,region,productid,productname,timestamp)

*/

product = LOAD '/home/px/Downloads/Semester2/nosql-project/product.log' USING PigStorage(' ') as (LOGLEVEL: chararray, DATE: chararray, TIMESTAMP: chararray, USERID: chararray, AGE: chararray, GENDER: chararray, REGION: chararray, OPERATION: chararray, PRODUCTID: chararray, PRODUCTNAME: chararray, ORDERID: chararray, PAYMENTMETHOD: chararray, COUPONNAME: chararray);

linlout = FILTER product BY OPERATION == 'LOGOUT' OR OPERATION == 'LOGIN';
filtered_linlout = FOREACH linlout GENERATE USERID, OPERATION, DATE, TIMESTAMP;
DUMP filtered_linlout;


/* Next Table Cart */

product = LOAD '/home/px/Downloads/Semester2/nosql-project/product.log' USING PigStorage(' ') as (LOGLEVEL: chararray, DATE: chararray, TIMESTAMP: chararray, USERID: chararray, AGE: chararray, GENDER: chararray, REGION: chararray, OPERATION: chararray, PRODUCTID: chararray, PRODUCTNAME: chararray, ORDERID: chararray, PAYMENTMETHOD: chararray, COUPONNAME: chararray);

cart = FILTER product BY OPERATION == 'CART-ADD' OR OPERATION == 'CART-REMOVE';
filtered_cart = FOREACH cart GENERATE USERID, AGE, REGION, PRODUCTID, PRODUCTNAME, DATE, TIMESTAMP, OPERATION;
DUMP filtered_cart;

/* Next Table  Purchase */

product = LOAD '/home/px/Downloads/Semester2/nosql-project/product.log' USING PigStorage(' ') as (LOGLEVEL: chararray, DATE: chararray, TIMESTAMP: chararray, USERID: chararray, AGE: chararray, GENDER: chararray, REGION: chararray, OPERATION: chararray, PRODUCTID: chararray, PRODUCTNAME: chararray, ORDERID: chararray, PAYMENTMETHOD: chararray, COUPONNAME: chararray);

purchase = FILTER product BY OPERATION == 'PURCHASE';
filtered_purchase = FOREACH purchase GENERATE USERID, AGE, REGION, PRODUCTID, PRODUCTNAME, DATE, TIMESTAMP, ORDERID, COUPONNAME, PAYMENTMETHOD;
DUMP filtered_purchase;

/* Next table product_view */

product = LOAD '/home/px/Downloads/Semester2/nosql-project/product.log' USING PigStorage(' ') as (LOGLEVEL: chararray, DATE: chararray, TIMESTAMP: chararray, USERID: chararray, AGE: chararray, GENDER: chararray, REGION: chararray, OPERATION: chararray, PRODUCTID: chararray, PRODUCTNAME: chararray, ORDERID: chararray, PAYMENTMETHOD: chararray, COUPONNAME: chararray);

pview = FILTER product BY OPERATION == 'PRODUCT-VIEWED';
filtered_pview = FOREACH pview GENERATE USERID, AGE, REGION, PRODUCTID, PRODUCTNAME, DATE, TIMESTAMP;
DUMP filtered_pview;


