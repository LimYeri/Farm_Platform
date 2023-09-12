from django.urls import path
from .views import *

urlpatterns = [
    # path("", home, name = "home"),
    # 농촌 뉴스 정보 등록
    path("newsCreate/", newsCreate, name = "newsCreate"),
    path("<int:news_id>/newsDetail", newsDetail, name = "newsDetail"),
    path("newsList/", newsList.as_view(), name = "newsList"),
    # 뉴스 수정
    path("<int:news_id>/newsEdit", newsEdit, name = "newsEdit"),
    # 뉴스 삭제
    path("<int:news_id>/deleteNews", deleteNews, name = "deleteNews"),
    # 기상 정보
    # path("weather", weather, name = "weather"),
    # 뉴스 좋아요
    path('<int:news_id>/likes/', likes, name='likes'),
    # 검색
    path("newsSearch/", newsSearch, name = "newsSearch"),
    
]