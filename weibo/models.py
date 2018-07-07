from django.db import models
from login.models import User
# Create your models here.
from django.contrib import admin

class Weibo(models.Model):
    content = models.CharField(max_length=150)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.content

admin.site.register(Weibo)