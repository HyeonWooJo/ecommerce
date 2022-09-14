from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.serializers import RegisterSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import SignInSerializer


class SignInView(APIView):
    """
    로그인 API
    :endpoint: /api/users/signgin
    :return: 로그인 성공여부
            access token
            refresh token
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignInSerializer(data=request.data)

        if serializer.is_valid():
            token = serializer.validated_data
            return Response(
                {
                    "message": "로그인 되었습니다.",
                    "access_token": token["access"],
                    "refresh_token": token["refresh"],
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class RegisterAPIView(CreateAPIView):
    """
    회원가입 API
    :endpoint: /api/users/register
    :return: username
            gender
            age
            id
    """
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeleteUserView(DestroyAPIView):
    """
    계정 삭제 API
    :endpoint: /api/users/delete/<int>
    :return: 없음
    """
    queryset = get_user_model().objects.all()