
from django.urls import path

from .views import RegisterAPIView, DeleteUserView, SignInView

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("delete/<int:pk>", DeleteUserView.as_view()),
    path("signin/", SignInView.as_view())
]