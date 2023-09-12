from django.urls import path
from . import views
# from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='index'), #홈
    path("login/", views.LoginView.as_view(), name="login2"), #로그인()
    path("login/kakao/", views.kakao_login, name="kakao-login"), # "Kakao Login" btn 경로
    path("login/kakao/callback", views.kakao_callback, name="kakao-callback"), # callback 경로
    path("logout/", views.log_out, name="logout"), #로그아웃
    path("signup/", views.SignUpView.as_view(), name="signup"), # 회원가입
    path('myfarm_love/',views.myfarm_love, name='myfarm_love'), #나의 농사랑방
    path('mypage/',views.mypage, name='mypage'), #mypage  다빈 수정 파일 매핑
    path('check_email/',views.check_email, name='check_email'), #이메일을 확인해봐라!!!
    path("verify/<str:key>", views.complete_verification, name="complete-verification"), #인증 메일 링크 클릭시 작동(실제 이메일 유효성 검사 함수)
    path('password_reset/', views.password_reset_request, name="password_reset"), #패스워드 초기화
]

