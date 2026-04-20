from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    def __str__(self):
        return self.category_name
    
class ProductModel(models.Model):
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    product_desc=models.CharField(max_length=100)
    product_price=models.IntegerField()
    product_image=models.ImageField(default='default.webp',upload_to='uploads')
    trending=models.BooleanField(default=0)
    offer=models.BooleanField(default=0)

class CartModel(models.Model):
    product_category=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    product_desc=models.CharField(max_length=100)   
    product_price=models.IntegerField()
    total_price=models.IntegerField(default=0)
    quantity=models.IntegerField(default=1)
    host=models.ForeignKey(User,on_delete=models.CASCADE)