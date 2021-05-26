from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #기초대사량
    RMR = models.FloatField()
    #권장칼로리
    RC = models.FloatField()
    #자신이 하고자하는 운동 시간
    exercise = models.FloatField()
