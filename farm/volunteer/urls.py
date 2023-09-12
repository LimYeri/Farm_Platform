from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.index, name='volunteerindex'),
    path('list/', views.volunteerlist, name='volunteerlist'),
    path('post/', views.post, name='post'),
    path('postlist/', views.post_list, name='post_list'),
    path('list/<int:pk>/', views.volunteer, name='volunteer'),
    path('<int:pk>/delete', views.volunteer_delete, name='volunteer_delete'),
    path('<int:pk>/modify', views.volunteer_modify, name='volunteer_modify'),
    path('<int:pk>/like', views.volunteer_like, name='volunteer_like'),
    path('likelist/', views.like_list, name='like_list'),
]