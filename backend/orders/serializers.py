from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Order, OrderDetail, Payment


class OrderDetailSerializer(serializers.ModelSerializer):
    """상세 주문 serializer"""
    class Meta:
        model = OrderDetail
        fields = '__all__'

    def create(self, validated_data):
        """
        - 상세 주문 객체 생성
        - 상세 주문 객체와 연결된 주문 객체의 total_price에 상세 주문 객체의 총 금액 더함
        """
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

    def update(self, instance, validated_data):
        """
        - 상세 주문 객체 수정
        - 상세 주문 객체와 연결된 주문의 total_price를 0으로 초기화
        - 주문과 연결된 상세 주문 객체들의 총 금액을 다 더함
        """
        instance.product_count  = validated_data['product_count']
        instance.product_option = validated_data['product_option']
        instance.save()

        order         = Order.objects.get(id=instance.order.id)
        order_details = OrderDetail.objects.filter(order=order)
        order.total_price = 0
        
        for order_detail in order_details:
            option_price  = order_detail.product_option.option_price
            product_count = order_detail.product_count
            total_price   = option_price * product_count

            order.total_price += total_price
        
        order.save()

        return order_detail


class OrderSerializer(serializers.ModelSerializer):
    """주문 serializer"""
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


class PaymentSerializer(serializers.ModelSerializer):
    """결제 serializer"""
    class Meta:
        model = Payment
        fields = [
            'method',
            'deposit_bank',
            'order'
        ]

    def create(self, validated_data):
        payment = Payment.objects.create(
            **validated_data
        )

        amount = Order.objects.get(id=payment.order).total_price
        payment.amount = amount
        payment.save()

        return payment