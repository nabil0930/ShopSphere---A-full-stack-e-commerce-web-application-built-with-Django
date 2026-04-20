from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from app1.views import *
# Create your views here.

def login_(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        u=authenticate(username=username,password=password)
        if u:
            login(request,u)
            return redirect('home')
        else:
            return render(request,'login_.html',{'wrong':True})


    return render(request,'login_.html',{'login_':True})

def register_(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        print(first_name,last_name,email,username,password,confirmpassword)

        if password!=  confirmpassword:
            return render(request,'register_.html',{'notmatch':True})
        
        elif (
            len(password)<8 or
            not any(i.isupper() for i in password)or
            not any(i.isdigit() for i in password)or
            not any(i in "!@#$%^&*_-<>?;:'{}\|()/*-+=" for i in password)
        ):
            return render(request,'register_.html',{'weak':True})
              
        try:
            u=User.objects.get(username=username)
            return render(request,'register_.html',{'status':True})
        
        except:
            u=User.objects.create(first_name=first_name,
                                  last_name=last_name,
                                  email=email,
                                  username=username,
                                  )
            u.set_password(password)
            u.save()
            return redirect('login_')

    return render(request,'register_.html',{'login_':True})

def logout_(request):
    logout(request)
    return redirect('home')

def profile(request):
    return render(request,'profile.html',{'profile':True,'count_cart':count_cart(request)})