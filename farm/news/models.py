from django.db import models
from Accounts.models import User


# Create your models here.
class News(models.Model):
    # 제목
    title = models.CharField(max_length=30)
    # 내용
    content = models.TextField()
    # 작성시간
    created_at = models.DateTimeField(auto_now_add=True)
    # 작성자
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 이미지
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    # 좋아요
    like_users = models.ManyToManyField(User, related_name='like_articles', null=True, blank=True)
    
    # DB table 이름 = posts
    class Meta:
        db_table = 'news'
    
    def get_absolute_url(self):
        return f'/news/{self.pk}'