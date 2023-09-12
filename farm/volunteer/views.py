from django.shortcuts import render, redirect
from .models import Volun
from tran.models import Tran
from django.urls import reverse

# Create your views here.

def index(request):
    if request.method == 'POST':
        type = request.POST['type']
        # URL 매개변수를 사용하여 productlist 페이지로 리다이렉트
        return redirect(reverse(volunteerlist, kwargs={'type': type}))
    return render(request, 'volun/volun.html')

def volunteerlist(request,):
    region = request.GET.get('region')
    regions = Volun.objects.all()
    if request.method =='POST':
        searched = request.POST['searched']
        posts = Volun.objects.filter(title__contains = searched)
        if region:
            posts = Volun.objects.filter(region=region, title__contains=searched)
        else:
            posts = Volun.objects.filter(title__contains=searched)
        return render(request,'volun/volunteer-list.html',{'searched':searched, 'posts':posts,'region':region, 'regions':regions})
    else:
        if region:
            postlist = Volun.objects.filter(region=region)
        else:
            postlist = Volun.objects.all()
        return render(request,'volun/volunteer-list.html', {'postlist':postlist,'region':region, 'regions':regions})
    
def volunteer(request, pk):
    writer = request.user.last_name
    post = Volun.objects.get(pk = pk)
    posts = Volun.objects.filter(region = post.region).exclude(pk=pk)
    if post.writer == writer:
        check = True
    else:
        check = False
    return render(request, 'volun/volunteer-detail.html',{'post':post, 'posts':posts, 'check':check})

def post(request):
    if request.method == 'POST':
        writer = request.user
        if request.FILES['image']:
            new_volunteer = Volun.objects.create(
                region = request.POST['region'],
                title = request.POST['title'],
                writer = writer,
                image = request.FILES['image'],
                start_period = request.POST['start_period'],
                end_period = request.POST['end_period'],
                hours = request.POST['hours'],
                contents = request.POST['contents'],
            )
        return redirect('/volunteer/')
    else:
        volun = Volun()
        return render(request, 'volun/write-post.html')
    
def volunteer_delete(request,pk):
    writer = request.user
    volunteer = Volun.objects.get(pk=pk)

    if volunteer.writer == writer:
        volunteer.delete()
        return redirect('/volunteer/')
    else:
        return redirect(f'/volunteer/list/{pk}')
    
def volunteer_modify(request, pk):
    writer = request.user
    volunteer = Volun.objects.get(pk=pk)
    if writer != volunteer.writer:
        return redirect(f'/volunteer/list/{pk}')
    if request.method == 'POST':
        volunteer.region = request.POST['region']
        volunteer.title = request.POST['title']
        volunteer.image = request.FILES['image']
        volunteer.hours = request.POST['hours']

        volunteer.start_period = request.POST['start_period']
        volunteer.end_period = request.POST['end_period']

        
        volunteer.contents = request.POST['contents']

        volunteer.save()

        return redirect('/volunteer/')
    else:
        volun = Volun()
        return render(request, 'volun/modify.html')
    
def post_list(request):
    if request.method =='POST':
        user = request.user
        searched = request.POST['searched']
        posts = Volun.objects.filter(title__contains = searched, writer=user)
        return render(request,'volun/postlist.html',{'searched':searched, 'posts':posts })
    else:
        user = request.user
        posts = Volun.objects.filter(writer=user)
        return render(request,'volun/postlist.html',{'posts':posts })
    
def volunteer_like(request, pk):
    if request.user.is_authenticated:
        post = Volun.objects.get(pk = pk)
        if post.like_users.filter(pk = request.user.pk).exists():
            post.like_users.remove(request.user)
        else:
            post.like_users.add(request.user)
        return redirect(f'/volunteer/list/{pk}')
    return redirect('/volunteer/')

def like_list(request):
    posts = Volun.objects.filter(like_users = request.user)
    return render(request, 'volun/wishlist.html',{'posts':posts})
