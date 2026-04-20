from django.shortcuts import render,redirect
from app1.models import ProductModel,Category,CartModel
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def count_cart(request):
    return CartModel.objects.filter().count()


def home(request):

    trend=False
    offer=False
    all_category=Category.objects.all()   #fetching all category

    if 'q' in request.GET:
        q=request.GET['q']

        try:
            cat=Category.objects.get(category_name__icontains=q)
            all_products=ProductModel.objects.filter(Q(product_category=cat))
        except:
            all_products=ProductModel.objects.filter(Q(product_name__icontains=q)|Q(product_desc__icontains=q))
            print(bool(all_products)) 
            print(all_products)     

    elif 'cat' in request.GET:
        cat=request.GET['cat']
        cat=Category.objects.get(category_name__icontains=cat)
        all_products=ProductModel.objects.filter(product_category=cat)

    elif 'trending' in request.GET:
        all_products=ProductModel.objects.filter(trending=True)
        trend=True

    elif 'offer' in request.GET:
        all_products=ProductModel.objects.filter(offer=True)
        offer=True

    else:
        all_products=ProductModel.objects.all()
        
    

    return render(request,'home.html',{'products':all_products,'Category':all_category,"trend":trend,"offer":offer,'count_cart':count_cart(request)})




def about(request):
    return render(request,'about.html',{'count_cart':count_cart(request)})


@login_required(login_url='login_')
def addtocart(request,pk):
    # product
    pro=ProductModel.objects.get(id=pk)
    print(pro.product_category)

    try :
        c=CartModel.objects.get(product_name=pro.product_name,host=request.user)
        c.quantity+=1
        c.total_price+=c.product_price
        c.save()
        return redirect('cart')
    
    except:
        CartModel.objects.create(
            product_category=pro.product_category,
            product_name=pro.product_name,
            product_desc=pro.product_desc,
            product_price=pro.product_price,
            quantity=1,
            total_price=pro.product_price,
            host=request.user
        )
        return redirect('home')


def delete_(request,pk):
    # cart data
    cart=CartModel.objects.get(id=pk)

    cart.delete()
    return redirect('cart')


@login_required(login_url='login_')
def cart(request):
    cart=CartModel.objects.filter(host=request.user)
    # add total
    total=sum(i.total_price for i in cart)
    
    return render (request,'cart.html',{'cart':cart,'total':total,'carts':True,'count_cart':count_cart(request)})






######################### ADD PRODUCT  #######################################


def add_products(request):

    all_category=Category.objects.all()

    if request.method =='POST':
        product_category=request.POST['category_attr']
        product_name=request.POST['product_name']
        product_desc=request.POST['product_desc']
        product_price=request.POST['product_price']
        product_image=request.FILES.get('product_image','default.webp')
        print(product_category,
              product_name,
              product_desc,
              product_price,
              product_image)
        
        pk_cat_mod=Category.objects.get(category_name=product_category)
        
        ProductModel.objects.create(
            product_category=pk_cat_mod,
            product_name=product_name,
            product_desc=product_desc,
            product_price=product_price,
            product_image=product_image
        )
        return redirect('home')


    return render(request,'add_products.html',{'category':all_category})