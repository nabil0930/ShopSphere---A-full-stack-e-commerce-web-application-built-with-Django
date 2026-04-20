from django.urls import path
from authuser import views

urlpatterns=[
    path('login_',views.login_,name='login_'),
    path('register_',views.register_,name='register_'),
    path('profile',views.profile,name='profile'),
    path('logout_',views.logout_,name='logout_'),

]