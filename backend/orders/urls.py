from django.urls import path
from .views import (
    OrderViewSet,
    OrderDetailViewSet,
    PaymentViewSet
)

order_list = OrderViewSet.as_view({
    'get'  : 'list',
    'post' : 'create'
})
order_detail = OrderViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'delete' : 'destroy'
})

detail_list = OrderDetailViewSet.as_view({
    'get'  : 'list',
    'post' : 'create'
})
detail_detail = OrderDetailViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'delete' : 'destroy'
})

payment_list = PaymentViewSet.as_view({
    'get'  : 'list',
    'post' : 'create'
})
payment_detail = PaymentViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'delete' : 'destroy'
})

urlpatterns = [
    path('', order_list, name='order-list'),
    path('<int:pk>/', order_detail, name='order-detail'),
    path('detail/', detail_list, name='detail-list'),
    path('detail/<int:pk>/', detail_detail, name='detail-detail'),
    path('payment/', detail_list, name='payment-list'),
    path('payment/<int:pk>/', detail_detail, name='payment-detail')
]