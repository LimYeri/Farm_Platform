from django.db import models

# Create your models here.
class Volun(models.Model):
    REGION_TYPE = {
        ('seoul', '서울'),
        ('metropolitan', '광역시'),
        ('gyeonggi', '경기도'),
        ('gangwon', '강원도'),
        ('chungcheong', '충청도'),
        ('jeolla', '전라도'),
        ('gyeongsong', '경상도'),
        ('jeju', '제주도'),
    }
    id = models.AutoField(primary_key=True)
    region = models.CharField(max_length=400, choices=REGION_TYPE, null=True)
    like_users = models.ManyToManyField('Accounts.User', blank=True, related_name='like_users')
    title = models.CharField(max_length=100, null = True)
    writer = models.ForeignKey('Accounts.User', on_delete=models.CASCADE, verbose_name='wrtier')
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name = '업로드일')
    image = models.ImageField(upload_to = "images/", blank=True, null=True)
    start_period = models.DateField(max_length=64, verbose_name='start period')
    end_period = models.DateField(max_length=64, verbose_name='end period')
    hours = models.IntegerField()
    contents = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'volunteer'
        verbose_name = 'volunteer'