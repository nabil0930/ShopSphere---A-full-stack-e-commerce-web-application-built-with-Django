from django.urls import path
from delivery import views

urlpatterns=[
    path('delivery',views.delivery,name='delivery'),
    path('update/<int:pk>',views.update,name='update'),
    path('ddelete/<int:pk>',views.ddelete,name='ddelete'),
    path('orders',views.orders,name='orders')

]