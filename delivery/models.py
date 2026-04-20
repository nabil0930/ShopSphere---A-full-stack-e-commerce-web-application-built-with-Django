from django.db import models

# Create your models here.
class DeliveryModel(models.Model):
    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    customer_address=models.CharField(max_length=500)
    customer_mob=models.IntegerField(max_length=13)