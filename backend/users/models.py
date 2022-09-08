from django.db import models
from core.models import TimeStampModel

class User(TimeStampModel):
    email   = models.EmailField(max_length=120)
    psword  = models.CharField(max_length=100)
    name    = models.CharField(max_length=50)
    address = models.CharField(max_length=120)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email