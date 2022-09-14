from django.db import models

from core.models     import TimeStampModel
from users.models    import User
from products.models import ProductOption


class Order(TimeStampModel):
    """
    주문 모델
    """
    total_price  = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'orders'

    def __str__(self):
        return self.id


class OrderDetail(models.Model):
    """
    주문 상세 모델
    """
    product_count  = models.PositiveIntegerField()
    product_option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    order          = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'orders_details'

    def __str__(self):
        return self.id


class Payment(TimeStampModel):
    """
    결제 모델
    """
    method       = models.CharField(max_length=80)
    amount       = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    deposit_bank = models.CharField(max_length=120)
    order        = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = 'payments'

    def __str__(self):
        return self.id