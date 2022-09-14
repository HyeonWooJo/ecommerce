from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Order, OrderDetail, Payment
from .serializers import (
    OrderSerializer,
    OrderDetailSerializer,
    PaymentSerializer
)
from .permissions import (
    OwnerAndStaffOrReadOnly_1,
    OwnerAndStaffOrReadOnly_2
)


class OrderViewSet(viewsets.ModelViewSet):
    """주문 CRUD API"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [OwnerAndStaffOrReadOnly_2]


class OrderDetailViewSet(viewsets.ModelViewSet):
    """상세 주문 CRUD API"""
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [OwnerAndStaffOrReadOnly_1]


class PaymentViewSet(viewsets.ModelViewSet):
    """결제 CRUD API"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [OwnerAndStaffOrReadOnly_1]