from django.views.generic import FormView
from django.shortcuts import redirect, render, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms, models 
from Board.models import Board
from django.urls import reverse_lazy
import os  #.env 값을 가져오기 위해 import
import requests
from django.http import HttpResponse


from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


#시작화면
def splash(request):
    return render(request,'User/splash.html')

#전체 홈
def index(request):
    return render(request, 'User/index.html')

#로그인
class LoginView(FormView):
    template_name = "User/login1.html"
    form_class = forms.LoginForm
    success_url = "/accounts"
    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None and user.email_verified is True: #회원이 아니거나 이메일 인증이 되지 않은 사용자는 로그인 불가
            login(self.request, user)
        else:
            return HttpResponse("인증되지 않은 사용자입니다. 계정을 활성화 하려면 이메일을 확인하십시오.")
        return super().form_valid(form) # super().form_valid(form)을 반환
    
#카카오 로그인
def kakao_login(request):
    client_id = os.environ.get("KAKAO_ID")
    redirect_uri = "http://127.0.0.1:8000/accounts/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
    )
    
class KakaoException(Exception): #  에러처리
    pass
def kakao_callback(request):
    try:
        code = request.GET.get("code") # 임시 코드 받기
        client_id = os.environ.get("KAKAO_ID")
        redirect_uri = "http://127.0.0.1:8000/accounts/login/kakao/callback"
        token_request = requests.get( #  code로 access_token을 JSON형태로 요청
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}" 
        )
        print(token_request.json())
        token_json = token_request.json()
        error = token_json.get("error", None)
        if error is not None: #  token 값이 없다면,
            raise KakaoException()
        access_token = token_json.get("access_token") #  access_token 추출
        profile_request = requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        ) # 👈 "access_token"으로 API(profile) 요청
        profile_json = profile_request.json()
        email = profile_json.get("kakao_account").get("email") #  email 값 
        if email is None: #  email이 없다면 에러 발생
            raise KakaoException()
        properties = profile_json.get("kakao_account").get("profile")
        nickname = properties.get("nickname") # 이름값
        print(nickname) 
        try:
            user = models.User.objects.get(email=email) 
            if user.login_method != models.User.LOGIN_KAKAO:
                raise KakaoException() 
        except models.User.DoesNotExist: # DB 확인-> 없다면 계정 생성
            user = models.User.objects.create(
                email=email,
                first_name=nickname,
                username=email,
                login_method=models.User.LOGIN_KAKAO,
                email_verified=True,
            )
            user.set_unusable_password()
            user.save()
        login(request, user)
        return redirect(reverse("index"))
    except KakaoException:
        return redirect(reverse("login"))
        # return HttpResponse("카카오 회원가입 오류")

#로그아웃
def log_out(request):
    logout(request)
    # return redirect('index')
    return redirect('login2')    

# def check_email(request):
#     return render(request, 'User/check-email.html')

#수정
def check_email(request):
    return render(request, 'User/check-email1.html')


# #회원가입(이메일 인증X ver.)
# class SignUpView(FormView):
#     template_name = "User/signup.html"
#     form_class = forms.SignUpForm
#     success_url = "/accounts" #이건 홈으로 보내는 거임
#     def form_valid(self, form): # form 받기
#         form.save() #  form 저장
#         email = form.cleaned_data.get("email")
#         password = form.cleaned_data.get("password")
#         user = authenticate(self.request, username=email, password=password)
#         if user is not None:
#             login(self.request, user)
#         return super().form_valid(form)
    
#회원가입(이메일 인증 ver.)
class SignUpView(FormView):
    template_name = "User/register.html"
    form_class = forms.SignUpForm
    # success_url = "/accounts" #이건 홈으로 보내는 거임
    success_url = reverse_lazy('check_email') 
    def form_valid(self, form): # form 받기
        form.save() #  form 저장
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None and user.email_verified is True:
            login(self.request, user)
        user.verify_email() # users/models.py의 verify_email() 실행
        return super().form_valid(form)
    

def complete_verification(request, key):
    try:
        user = models.User.objects.get(email_secret=key) #  uuid값을 기준으로 Object 가져옴
        user.email_verified = True 
        user.email_secret = ""
        user.save()
        # to do: add succes message
        # return redirect('index') 
        # return HttpResponse("OKAY")
        return redirect(reverse('login2')) 
    except models.User.DoesNotExist:
        return HttpResponse("User does not exist") 
        # pass
        # return redirect(reverse('index'))    
    
#나의 농사랑방
def myfarm_love(request):
    id=request.user
    Boardlist=Board.objects.filter(user=id) #해당 사용자 세션 기준으로 게시글 뽑기
    Boardlist=Boardlist.order_by('-id') #게시글 최신순 정렬
    # return render(request, 'User/farm_love.html', {'Boardlist':Boardlist})   
    return render(request, 'Board/MyBoardList.html', {'Boardlist':Boardlist})

#마이페이지
def mypage(request):
    # id=request.user
    # Boardlist=Board.objects.filter(user=id) #해당 사용자 세션 기준으로 게시글 뽑기
    # Boardlist=Boardlist.order_by('-id') #게시글 최신순 정렬
    return render(request, 'User/mypage.html') 


#비밀번호 변경
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = get_user_model().objects.filter(Q(email=data))  #이메일로 회원 조회
			if associated_users.exists():
				for user in associated_users:
					subject = '[FARM] 비밀번호 재설정'
					email_template_name = "account/password_reset_email.html"
                    # email_template_name = "account/password_reset_email.txt"
					c = {
						"email": user.email,
						"uid": urlsafe_base64_encode(force_bytes(user.pk)),
						"user": user,
						# Return a token that can be used once to do a password reset for the given user.
						'token': default_token_generator.make_token(user),
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, settings.EMAIL_FROM,[user.email], fail_silently=False,html_message=email)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(
		request=request,
		template_name='account/password_reset.html',
		context={'password_reset_form': password_reset_form})
