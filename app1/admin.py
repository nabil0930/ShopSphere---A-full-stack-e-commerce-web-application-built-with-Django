from django.contrib import admin

# Register your models here.
from app1.models import ProductModel,Category

class ProductsAdminModel(admin.ModelAdmin):
    list_display=[
        'product_category',
        'product_name',
        'product_desc',
        'product_price',
    ]
admin.site.register(ProductModel,ProductsAdminModel)

class CategoryAdminModel(admin.ModelAdmin):
    list_display=['category_name']
admin.site.register(Category,CategoryAdminModel)