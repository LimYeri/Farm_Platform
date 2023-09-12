# users/forms.py
from django import forms
from . import models

class LoginForm(forms.Form): #  가장 기본적인 form인 Form을 상속
    """Login Form Definition"""
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput) #  widget을 이용하면 form의 style을 변경
    
    def clean(self):
        email = self.cleaned_data.get("email") #  유효성 검사를 진행한 email field 값 추출
        password = self.cleaned_data.get("password") #  유효성 검사를 진행한 password field 값 추출
        try:
            user = models.User.objects.get(email=email) #  emil을 기준으로 해당 Object 가져오기
            if user.check_password(password):  #  비밀번호가 서로 일치 True, 아니면 False 반환
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))
            
            
class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            "first_name",
            "last_name",
            "email",
        )
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password
    def save(self, *args, **kwargs): #  save 매서드 가로채기
        user = super().save(commit=False) #  Object는 생성하지만, 저장X
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password) #  set_password는 비밀번호를 해쉬값으로 변환
        user.save() # 저장