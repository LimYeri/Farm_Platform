from django.shortcuts import render, redirect
from .models import Tran
from django.urls import reverse
# from volunteer.models import Volun

# Create your views here.
def index(request):
    if request.method == 'POST':
        type = request.POST['type']
        # URL 매개변수를 사용하여 productlist 페이지로 리다이렉트
        return redirect(reverse(productlist, kwargs={'type': type}))
    return render(request, 'trans/market.html')
    
def productlist(request):
    type = request.GET.get('type')
    types = Tran.objects.all()
    if request.method =='POST':
        searched = request.POST['searched']
        products = Tran.objects.filter(productname__contains = searched)
        if type:
            products = Tran.objects.filter(type=type, productname__contains=searched)
        else:
            products = Tran.objects.filter(productname__contains=searched)
        return render(request,'trans/product-list.html',{'searched':searched, 'products':products,'type':type, 'types':types})
    else:
        if type:
            productlist = Tran.objects.filter(type=type)
        else:
            productlist = Tran.objects.all()
        return render(request,'trans/product-list.html', {'productlist':productlist,'type':type, 'types': types})

def product(request, pk):
    seller = request.user
    product = Tran.objects.get(pk = pk)
    products = Tran.objects.filter(productname = product.productname).exclude(pk=pk)
    if product.seller == seller:
        check = True
    else:
        check = False
    return render(request, 'trans/product-detail.html',{'product':product, 'products':products, 'check':check})

def post(request):
    if request.method == 'POST':
        seller = request.user
        if request.FILES['image']:
            new_product = Tran.objects.create(
                type = request.POST['type'],
                productname = request.POST['productname'],
                seller = seller,
                image = request.FILES['image'],
                price = request.POST['price'],
                contents = request.POST['contents'],
            )
        return redirect('tranindex')
    else:
        tran = Tran()
        return render(request, 'trans/write-post.html')

def product_delete(request,pk):
    seller = request.user
    product = Tran.objects.get(pk=pk)

    if product.seller == seller:
        product.delete()
        return redirect('tranindex')
    else:
        return redirect(f'/tran/list/{pk}')
    
def product_modify(request, pk):
    seller = request.user
    product = Tran.objects.get(pk=pk)
    if seller != product.seller:
        return redirect(f'/tran/list/{pk}')
    
    if request.method == 'POST':
        product.type = request.POST['type']
        product.productname = request.POST['productname']
        product.image = request.FILES['image']
        product.price = request.POST['price']
        product.contents = request.POST['contents']
        product.save()

        return redirect('tranindex')
    else:
        tran = Tran()
        return render(request, 'trans/modify.html')
    
def post_list(request):
    if request.method =='POST':
        user = request.user
        searched = request.POST['searched']
        products = Tran.objects.filter(productname__contains = searched, seller = user)
        return render(request,'tran/postlist.html',{'searched':searched, 'products':products})
    else:
        user = request.user
        productlist = Tran.objects.filter(seller=user)
        return render(request,'tran/postlist.html', {'productlist':productlist})

# 좋아요
# @login_required
def product_like(request, pk):
    if request.user.is_authenticated:
        product = Tran.objects.get(pk = pk)
        if product.like_user.filter(pk = request.user.pk).exists():
            product.like_user.remove(request.user)
        else:
            product.like_user.add(request.user)
        return redirect(f'/tran/list/{pk}') 
    return redirect('tranindex')

def like_list(request):
    products = Tran.objects.filter(like_user = request.user)
    return render(request, 'trans/wishlist.html',{'products':products})


    
    