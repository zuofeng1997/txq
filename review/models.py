from django.db import models
# from ..weibo.models import Weibo
# from txq.login.models import User
# Create your models here.
from weibo.models import  Weibo
from login.models import User
from django.contrib import admin

class Review(models.Model):
    review = models.CharField(max_length=100)   #评论内容
    weibo = models.ForeignKey(Weibo,on_delete=models.CASCADE)   #评论的微博
    user = models.ForeignKey(User,on_delete=models.CASCADE)    #评论的用户
    def __str__(self):
        return self.review
admin.site.register(Review)
