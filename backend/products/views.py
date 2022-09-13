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
        return self.list(request, *args, **kwargs)

    @login_decorator
    def post(self, request, *args, **kwargs):
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
        return self.retrieve(request, *args, **kwargs)
    
    @login_decorator
    def put(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise ValidationError('권한이 없습니다.')
        return self.update(request, *args, **kwargs)
    
    @login_decorator
    def delete(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise ValidationError('권한이 없습니다.')
        return self.delete(request, *args, **kwargs)