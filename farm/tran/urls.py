from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.index, name='tranindex'),
    path('list/', views.productlist, name='productlist'),
    path('post/', views.post, name='tranpost'),
    path('postlist/', views.post_list, name='post_list'),
    path('list/<int:pk>/', views.product, name='product'),
    path('<int:pk>/delete', views.product_delete, name='product_delete'),
    path('<int:pk>/modify', views.product_modify, name='product_modify'),
    path('<int:pk>/like', views.product_like, name='product_like'),
    path('likelist/', views.like_list, name='like_list'),
]


