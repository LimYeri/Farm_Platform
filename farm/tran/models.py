from django.db import models

# Create your models here.
class Tran(models.Model):
    PRODUCT_TYPE = {
        ('fruits', '과일'),
        ('grain', '곡물'),
        ('herbs', '나물'),
        ('mushroom', '버섯'),
        ('nuts', '견과류'),
        ('root', '뿌리'),
        ('vegetable', '채소'),
        ('non-specified', '기타 작물'),
    }
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=400, choices=PRODUCT_TYPE, null=True)
    like_user = models.ManyToManyField('Accounts.User', blank=True, related_name='like_user')
    productname = models.CharField(max_length=100, null = True)
    seller = models.ForeignKey('Accounts.User', on_delete=models.CASCADE, verbose_name='판매자')
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name = '업로드일')
    image = models.ImageField(upload_to = "images/", blank=True, null=True)
    price = models.CharField(max_length=10)
    contents = models.TextField()

    def __str__(self):
        return self.productname
    
    class Meta:
        db_table = 'post'
        verbose_name = 'product'


# class Cart(models.Model):
#     user = models.ForeignKey('Accounts.User', on_delete=models.CASCADE)
#     like_product = models.ManyToManyField('Tran', blank=True, related_name='like_product')

#     def __str__(self):
#         return str(self.user)