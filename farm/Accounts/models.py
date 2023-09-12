from django.db import models
from django.contrib.auth.models import AbstractUser #  AbstractUser를 import
import uuid #  "uuid" import
from django.conf import settings  #  "settings.py" import
from django.core.mail import send_mail #  "send_mail" import
from django.utils.html import strip_tags #  "strip_tags" import
from django.template.loader import render_to_string #  "render_to_string" import

class User(AbstractUser):
    pass

    
    #소셜 로그인
    LOGIN_EMAIL = "email"  #  choices에 들어갈 목록 생성
    LOGIN_KAKAO = "kakao"
    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_KAKAO, "Kakao"),
    )
    
    login_method = models.CharField(
     max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    ) #  login_method 필드로 LOGIN_CHOICES 저장
    #이메일 인증
    email_verified = models.BooleanField(default=False)  #  인증여부(True, False)
    email_secret = models.CharField(max_length=120, default="", blank=True)  #  uuid를 사용하여 난수 임시 저장
    def verify_email(self): #  회원가입 시, email을 인증을 위한 매서드
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20] #  random key 생성
            self.email_secret = secret  #  random key를 DB에 저장
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                "Verify Farm Account",  #  제목
                strip_tags(html_message),  # 내용
                settings.EMAIL_FROM,  #  발송자
                [self.email],  #  수신자
                fail_silently=False, 
                html_message=html_message,  #  html을 메일로 전송
            )
            self.save()
        return