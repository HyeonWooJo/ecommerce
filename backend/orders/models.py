from django.db import models

from core.models     import TimeStampModel
from users.models    import User
from products.models import ProductOption

class Order(TimeStampModel):
    """
    주문 모델
    """
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return self.id


class OrderDetail(models.Model):
    """
    주문 상세 모델
    """
    product_count   = models.PositiveIntegerField()
    order           = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_options = models.ForeignKey(ProductOption, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return self.id


class Payment(TimeStampModel):
    """
    결제 모델
    """
    method       = models.PositiveIntegerField()
    amount       = models.DecimalField(max_digits=8, decimal_places=2)
    deposit_bank = models.CharField(max_length=120)
    order        = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return self.id