from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Order, OrderDetail, Payment


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

    def create(self, validated_data):
        order_detail = OrderDetail.objects.create(
            **validated_data
        )
        order = Order.objects.get(id=order_detail.order.id)
        
        option_price  = order_detail.product_option.option_price
        product_count = order_detail.product_count
        total_price   = option_price * product_count

        order.total_price += total_price
        order.save()

        return order_detail


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    detail = serializers.SerializerMethodField()

    def get_detail(self, obj):
        """order 내 order_detail 조회"""
        order_details = obj.orderdetail_set.all()
        return OrderDetailSerializer(
                instance=order_details, 
                many=True,
                context=self.context
                ).data