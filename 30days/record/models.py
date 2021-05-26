from django.db import models
from django.contrib.auth.models import User

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #오늘 하루 섭취한 칼로리
    calorie = models.FloatField()
    #운동종류
    exercise = models.CharField(max_length=200)
    #오늘 하루 운동 시간
    exerciseTime = models.FloatField()
    #코멘트
    comment = models.TextField()
    #글 작성 날짜
    create_date = models.DateTimeField()
    

