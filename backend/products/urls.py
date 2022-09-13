
from django.urls import path, include
from . import views

urlpatterns = [
    # Mixin
    path('mixin/post/', views.ProducttListMixins.as_view()),
    path('mixin/post/<int:pk>/', views.ProductDetailMixins.as_view()),
]