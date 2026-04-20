from django.urls import path
from app1 import views

urlpatterns=[
    path('',views.home,name='home'),

    path('about',views.about,name='about'),
    path('cart',views.cart,name='cart'),
    path('addtocart/<int:pk>',views.addtocart,name='addtocart'),
    path('delete_/<int:pk>',views.delete_,name='delete_'),
    path('count_cart',views.count_cart,name='count_cart'),


    path('add_products',views.add_products,name='add_products'),
]