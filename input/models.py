from django.db import models

# Create your models here.


#电影表
class Movie_list(models.Model):
    name = models.CharField(max_length=1000)#电影名字
    rating_num = models.CharField(max_length=1000)#评分数字

    def __str__(self):
        return self.name

#短评表
class Content(models.Model):
    mid = models.ForeignKey(Movie_list,on_delete=models.CASCADE)  # 关联电影名字 id
    realname =  models.CharField(max_length=640) # 姓名
    short = models.CharField(max_length=10000)# 电影短评



    def __str__(self):
        return self.realname
