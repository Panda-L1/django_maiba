from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True,verbose_name='文章id')
    title = models.CharField(max_length=100,verbose_name='文章标题')
    content = models.TextField(verbose_name='文章内容')
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name='作者'
    )
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    remark_num = models.IntegerField(default=0,verbose_name='评论数')
    click_num = models.IntegerField(default=0,verbose_name='点击数')
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'article'
