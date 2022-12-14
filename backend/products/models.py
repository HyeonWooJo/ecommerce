from distutils.command.upload import upload
from django.db import models

from core.models import TimeStampModel
from core.image  import image_upload_path


class Product(TimeStampModel):
    """상품 모델"""
    name    = models.CharField(max_length=120)
    price   = models.DecimalField(max_digits=8, decimal_places=2)
    content = models.TextField()
    origin  = models.CharField(max_length=40)
    quantity = models.IntegerField()
    
    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    """상품 옵션 모델"""
    product      = models.ForeignKey(Product, on_delete=models.CASCADE)
    option_name  = models.CharField(max_length=70)
    option_price = models.DecimalField(max_digits=8, decimal_places=2)
    
    class Meta:
        db_table = 'products_options'

    def __str__(self):
        return self.option_name


class ProductImage(models.Model):
    """상품 이미지 모델"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_thumbnail = models.BooleanField(default=False)
    image = models.ImageField(upload_to=image_upload_path)
    
    class Meta:
        db_table = 'products_imagess'

    def __str__(self):
        return self.product