from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class PostAdd(models.Model):
    delete_post=models.ForeignKey(User,on_delete=models.CASCADE,default="1")
    new_post=models.CharField(max_length=10000000000,default="")
    heading=models.CharField(max_length=200,default="")
    pub_date=models.DateTimeField(auto_now=True)
    author=models.CharField(max_length=200)
    random_link=models.CharField(max_length=200,default="",blank=True, null=True)
    post_image=models.ImageField(upload_to='images/',default="",blank=True,null=True)

class UserSignup(models.Model):
    delete_user=models.ForeignKey(User,on_delete=models.CASCADE,default="1")
    profile_image=models.ImageField(upload_to='images/',default="",null=True,blank=True)
