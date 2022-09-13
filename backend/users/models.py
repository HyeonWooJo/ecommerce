from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from core.models     import TimeStampModel
from products.models import Product


class User(TimeStampModel):
    """
    유저 모델
    """
    email   = models.EmailField(max_length=120)
    psword  = models.CharField(max_length=100)
    name    = models.CharField(max_length=50)
    address = models.CharField(max_length=120)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email


class Comment(TimeStampModel):
    """
    댓글 모델
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'comments'

    def __str__(self):
        return self.product