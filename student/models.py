from enum import Enum
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class BaseModel(models.Model):

    class Meta:
        abstract = True

    ct = models.DateTimeField(verbose_name="创建日期", auto_now_add=True)
    mt = models.DateTimeField(verbose_name="变更日期", auto_now=True)
class ClassModel(BaseModel):
    #请根据题目说明自行补全完整的Model
    name :str = models.CharField(verbose_name="班级名称",max_length=64,help_text="班级名称")

class SEX(str, Enum):
    MALE = 1
    FEMALE = 0

class StudentModel(BaseModel):
    #请根据题目说明自行补全完整的Model
    user:User=models.OneToOneField(settings.AUTH_USER_MODEL,verbose_name="用户 与学生1:1",on_delete=models.CASCADE)#联级删除
    sex:SEX=models.SmallIntegerField(verbose_name="性别",choices=[(r.name,r.value) for r in SEX])
    cs:ClassModel = models.ForeignKey("ClassModel",on_delete=models.CASCADE) #联级删除