from django.urls import path
from . import views

urlpatterns = [
    path('',views.board, name='board'), #게시판 홈
    path('insert/',views.insert, name='insert'), #게시글 저장 함수
    path('detail/<int:pk>',views.detail, name='detail'),  #게시글 상세 정보 
    path('detail/<int:pk>/delete/',views.detail_delete, name='detail_delete'),  #게시글 상세 정보 
    path('detail/<int:pk>/edit/',views.detail_edit, name='detail_edit'),  #게시글 상세 정보 
    # path('mypage/',views.mypage, name='mypage'), #mypage
    path('<int:pk>/comment',views.comment_create, name='comment_create'), #댓글
    # path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:board_pk>/comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'), #댓글삭제
    path("search/", views.search, name = "search"), #게시글 검색
]