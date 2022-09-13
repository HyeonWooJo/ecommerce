from rest_framework import generics
from rest_framework import mixins
from rest_framework.exceptions import ValidationError

from .models import Product
from .serializers import ProductSerializer
from core.utils import login_decorator

class ProducttListMixins(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        """
        제품 리스트 조회 API
        endpoint: /api/products/mixin/post/
        """
        return self.list(request, *args, **kwargs)

    @login_decorator
    def post(self, request, *args, **kwargs):
        """
        제품 생성 API
        endpoint: /api/products/mixin/post/
        """
        if not request.user.is_staff:
            raise ValidationError('권한이 없습니다.')
        return self.create(request, *args, **kwargs)


class ProductDetailMixins(mixins.RetrieveModelMixin, 
                        mixins.UpdateModelMixin, 
                        mixins.DestroyModelMixin, 
                        generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        """
        제품 상세 조회 API
        endpoint: /api/products/mixin/post/<int:pk>/
        """
        return self.retrieve(request, *args, **kwargs)
    
    @login_decorator
    def put(self, request, *args, **kwargs):
        """
        제품 상세 수정 API
        endpoint: /api/products/mixin/post/<int:pk>/
        """
        if not request.user.is_staff:
            raise ValidationError('권한이 없습니다.')
        return self.update(request, *args, **kwargs)
    
    @login_decorator
    def delete(self, request, *args, **kwargs):
        """
        제품 상세 삭제 API
        endpoint: /api/products/mixin/post/<int:pk>/
        """
        if not request.user.is_staff:
            raise ValidationError('권한이 없습니다.')
        return self.delete(request, *args, **kwargs)