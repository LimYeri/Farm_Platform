from django.db import models
from Accounts.models import User
from django.conf import settings

class Board(models.Model):
    id=models.AutoField(primary_key=True) #게시글 id 값
    title=models.CharField(max_length=50, null=True,blank=True)   #제목
    date=models.DateTimeField(auto_now=True, null=True,blank=True)   #날짜
    content=models.TextField(blank=True, null=True)  #내용
    image = models.ImageField(max_length=255,upload_to='images/', blank=True, null=True)    #사진 업로드
    # # 좋아요
    # like_users = models.ManyToManyField(User, related_name='like_articles', null=True, blank=True)
    
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)#회원 삭제되면 다이어리도 함께 삭제됨.
    
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    cid=models.AutoField(primary_key=True) #댓글 id 값
    content=models.TextField() #댓글 내용
    date=models.DateTimeField(auto_now=True, null=True,blank=True)   #댓글 생성날짜
    # modified_time=models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    board=models.ForeignKey(Board, null=True, blank=True,on_delete=models.CASCADE) #댓글 작성할 게시글
    
    def __str__(self):
        return self.content

    