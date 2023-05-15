from django.shortcuts import render
#from pyhive import hive
#conn = hive.Connection(host='localhost',port='10000',database='hiveyagodb',username='hadoop')
#cursor = conn.cursor()
# Create your views here.
import json
from dashboard.models import *
from django.http import JsonResponse

def index(request):
    #cursor.execute("select distinct object from datastore where predicate='<hasGivenName>' and subject in (select subject from hiveyagodb.datastore where predicate='<livesIn>' group by subject having count(*) > 1)")
    #print(cursor.fetchall())
    return render(request, "index.html")

def product(request):
  return render(request, "product.html")

def productapi(request):


    data = DashboardStats.objects.all().order_by('-id')
    data = data[0].product_data


    return JsonResponse({'data':data})

def server(request):
  return render(request, "server.html")

def serverapi(request):

  data = DashboardStats.objects.all().order_by('-id')
  data = data[0].server_log_data


  return JsonResponse({'data':data})

def advertise(request):
  return render(request, "advertise.html")

def advertiseapi(request):

  data = DashboardStats.objects.all().order_by('-id')
  data = data[0].advertise_data  


  return JsonResponse({'data':data})
