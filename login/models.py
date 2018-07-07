from django.db import models
from django.contrib import admin

class User(models.Model):
    imageurl = models.CharField(max_length=100)   #图片路径
    username = models.CharField(max_length=20)  #用户名
    password = models.CharField(max_length=20)   #密码
    def __str__(self):
        return self.username

class Follow(models.Model):
    user1 = models.ForeignKey(User,related_name="user1",on_delete=models.CASCADE)
    user2 = models.ManyToManyField(User,blank=True,related_name="user2")
    def __str__(self):
        return self.user1.username
admin.site.register(User)
admin.site.register(Follow)
