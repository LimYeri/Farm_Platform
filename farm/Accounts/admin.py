# from django.contrib import admin
# from . import models # 👈 해당 model이 존재하는 파일을 import

# @admin.register(models.User) # 👈 데코레이터로 등록
# class CustomUserAdmin(admin.ModelAdmin):
#     pass

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # 👈 UserAdmin이 위치한 곳
from . import models
@admin.register(models.User)  
class CustomUserAdmin(UserAdmin): # 👈 UserAdmin 상속받음
    """Custom User Admin"""
    pass
