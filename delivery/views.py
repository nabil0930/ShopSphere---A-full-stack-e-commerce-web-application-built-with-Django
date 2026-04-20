from django.shortcuts import render,redirect
from app1.views import *
from app1.models import CartModel
from .forms import DeliveryForm
from django.contrib.auth.models import User
from delivery.models import DeliveryModel

# Create your views here.
def delivery(request):

    user_details=User.objects.get(username=request.user)
    cart_pro=CartModel.objects.filter(host=request.user)
    total=sum(i.total_price for i in cart_pro)

    if request.method=="POST":
        form=DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
        
    return render(request,'delivery_.html',{'delivery':delivery, 'count_cart':count_cart(request), 'form':DeliveryForm(instance=user_details),
    'data':DeliveryModel.objects.filter(username=request.user),'cart_pro':cart_pro,'total':total})

def update(request,pk):

    # old data
    data=DeliveryModel.objects.get(id=pk)

        
    if request.method=="POST":
        form=DeliveryForm(request.POST,data)
        if form.is_valid():
            form.save()
            return redirect('orders')

    context={'form':DeliveryForm(instance=data)}

    return render(request,'update.html',context)


def ddelete(request,pk):
    # user detail
    data=DeliveryModel.objects.get(id=pk)
    data.delete()
    return redirect('orders')

def orders(request,):
    cart_pro=CartModel.objects.all()
    cart_pro.delete()
    orderss=DeliveryModel.objects.all()

    return render(request,'order_placed.html',{'orders':orderss,'cart_pro':cart_pro})