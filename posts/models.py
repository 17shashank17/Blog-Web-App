from django.db import models

# Create your models here.

class PostAdd(models.Model):
    new_post=models.CharField(max_length=10000000000,default="")
    heading=models.CharField(max_length=200,default="")
    pub_date=models.DateTimeField(blank=True,null=True)
    author=models.CharField(max_length=200)
    random_link=models.CharField(max_length=200,default="",blank=True, null=True)
