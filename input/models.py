from django.db import models

# Create your models here.


# 电影表
class Movie_list(models.Model):
    name = models.CharField(max_length=1000)#电影名字
    rating_num = models.CharField(max_length=1000)#评分数字

    def __str__(self):
        return self.name

# 短评表
class Content(models.Model):
    mid = models.ForeignKey(Movie_list,on_delete=models.CASCADE)  # 关联电影名字 id
    realname =  models.CharField(max_length=640) # 姓名
    short = models.CharField(max_length=10000)# 电影短评



    def __str__(self):
        return self.realname

# 明细表
class Detailed(models.Model):
    type = models.CharField(max_length=16) # 类型 1 收入 2 支出
    store = models.CharField(max_length=64) # 门店
    price = models.CharField(max_length=16) # 金额
    remark =  models.CharField(max_length=64)  # 备注
    create_time =  models.DateTimeField(auto_now=True)  # 创建时间
    other =  models.CharField(max_length=64)  # 其他


    def __str__(self):
        return self.remark

# 数据表

