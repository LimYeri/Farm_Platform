# Create your views here.
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
import requests
from .models import *
# from pyowm import OWM
from django.db.models import Q

def newsCreate(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        img = request.FILES['newsImg']
        
        if request.user.is_authenticated:
            News.objects.create(
                title=title, 
                content=content, 
                img = img,
                author=author)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'NO'})
    else:
        # 게시글 등록 페이지 로딩
        return render(request, 'news/newsCreate.html')
    
class newsList(ListView):
    model = News
    # 게시글 pk값 기준 내림차순 정렬
    ordering = '-pk'
    template_name = 'news/newsList.html'
    
def newsDetail(request, news_id):
    # 해당 post_id에 맞는 객체 반환
    newsPost = get_object_or_404(News, id=news_id)
    # 해당 게시글 작성자와 현재 user가 같다면 
    if newsPost.author.id == request.user.id:
        # 게시글 수정 가능 태그 보이게 하기
        message = 'OK'
    else: message = 'NO'
    # 현재 게시글 정보, 댓글 정보, 유저 정보 반환 후 상세페이지 로딩
    return render(request, 'news/newsDetail.html', {"news": newsPost, "message": message})

def newsEdit(request, news_id):
    # 해당 post_id에 맞는 객체 반환
    newsPost = get_object_or_404(News, id=news_id)
    # 작성자와 현재 user가 같다면
    if newsPost.author.id == request.user.id :
        if request.method == 'POST':
            # 입력 값 저장
            newsPost.title = request.POST['title']
            newsPost.content = request.POST['content']
            newsPost.author = request.user
            # 게시글 수정
            newsPost.save()
            return redirect('home')
        # 수정 페이지 로딩
        else:
            return render(request, 'newsEdit.html', {'news': newsPost})
    # 수정 권한이 없으므로 에러 메시지 출력 후 메인 페이지 로딩
    # editError-NO : '회원님에게는 수정 및 삭제 권한이 없습니다.'
    else:
        return render(request, 'home.html', {'editError': 'NO'})

def deleteNews(request, news_id):
    # 해당 post_id에 맞는 객체 반환
    newsPost = get_object_or_404(News, id=news_id)
    # 작성자와 현재 user가 같다면
    if newsPost.author.id == request.user.id :
        # 게시글 삭제
        newsPost.delete()
        # 마이페이지 로딩
        return redirect('home')
    # 식제 권한이 없으므로 에러 메시지 출력 후 메인 페이지 로딩
    # editError-NO : '회원님에게는 수정 및 삭제 권한이 없습니다.'
    else:
        return render(request, 'home.html', {'editError': 'NO'})
    

def weather(request):
    appid = "0840a9fd4f902fab612b34d467592bf9"
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':'Seoul', 'appid':appid, 'lang':'kr', 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    print(res['main']['temp'])
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    
    return render(request, 'weather.html', {'description':description, 'icon':icon, 'temp':temp})
    
def likes(request, news_id):
    if request.user.is_authenticated:
        article = get_object_or_404(News, id=news_id)

        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect(newsDetail, news_id=news_id)
    return redirect('login')

def newsSearch(request):
    if request.method == 'POST':
        # 검색어 입력값 저장
        searched = request.POST['searched']
        title_s = News.objects.filter(Q(title__contains=searched) | Q(content__contains=searched))
        return render(request, 'news/newsList.html', {'news_list': title_s, 'searched':searched})
    else:
        return redirect('newsList')