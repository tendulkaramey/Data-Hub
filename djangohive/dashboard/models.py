from django.db import models
from django.utils.timezone import now

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    jsondata = models.JSONField(default={})

class DashboardStats(models.Model):
    product_data = models.JSONField(blank=True)
    server_log_data = models.JSONField(blank=True)
    advertise_data = models.JSONField(blank=True)
    created_at = models.DateTimeField(default=now)