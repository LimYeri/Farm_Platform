"""
URL configuration for farm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
import Accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',Accounts.views.LoginView.as_view()),
    path('',Accounts.views.splash),
    path('accounts/',include('Accounts.urls')),  #홈 화면 설정
    path('board/',include('Board.urls')),
    path('chat/',include('chat.urls')),
    path('news/',include('news.urls')),
    path('tran/',include('tran.urls')),
    path('volunteer/',include('volunteer.urls')),
    path('plus/',include('Plus.urls')),
    # path('password/', include('django.contrib.auth.urls')), #패스워드 변경 사용...
      path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

