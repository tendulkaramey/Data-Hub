from products_data import products_data
from users import users
import random
from random import randrange
from datetime import timedelta,datetime

#LOG-LEVEL TIMESTAMP USERID AGE GENDER REGION OPERATION PRODUCTID PRODUCTNAME ORDERID PAYMENTMETHOD COUPONNAME

def random_date(start= datetime.now()-timedelta(days=120), end=datetime.now()):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return str(start + timedelta(seconds=random_second))

operations=[
    'CART-ADD','PURCHASE','LOGIN','LOGOUT','COUPON-USED','PRODUCT-VIEWED','CART-REMOVE'
]

payment_methods=[
    'DEBIT-CARD','CREDIT-CARD','UPI','COD','PAYTM','ONLINE-BANKING'
]


user_atrtibutes=['id','age','gender','region']

coupon_names=[
    'SAVE10','SAVE50','SAVE20','OFFER32'
]



logs = []
userlength = len(users)-1
productslength = len(products_data)-1
operationlength = len(operations)-1
paymentlength = len(payment_methods)-1
couponlength = len(coupon_names)-1
for i in range(0,500000):
    randomuser=users[random.randint(0,userlength)]
    randomproduct=products_data[random.randint(0,productslength)]
    randomoperation=operations[random.randint(0,operationlength)]
    randomorderid=None
    randomproductid=randomproduct['id']
    randomproductname=randomproduct['name']
    randompayment=None
    randomcouponname=None
    if randomoperation == 'COUPON-USED':
        randomcouponname = coupon_names[random.randint(0,couponlength)]
    if randomoperation == 'PURCHASE' or randomoperation =='COUPON-USED':
        randompayment=payment_methods[random.randint(0,paymentlength)]
        randomorderid=random.randint(10000,300000)
    if randomoperation == 'LOGIN' or randomoperation == 'LOGOUT':
        randomproductid=None
        randomproductname=None
        randomorderid=None
    logrow='{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11}'.format('DEBUG',random_date(),randomuser['id'],randomuser['age'],randomuser['gender'],randomuser['region'],randomoperation,randomproductid,randomproductname,randomorderid,randompayment,randomcouponname)
    logs.append(logrow)

with open('product.log', 'w') as f:
    for line in logs:
        f.write(f"{line}\n")