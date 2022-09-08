from django.db import models

# 데이터 생성시간, 업데이트 시간 추상화 클래스
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True