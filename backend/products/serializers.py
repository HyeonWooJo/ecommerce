from django.db import transaction

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Product, ProductImage, ProductOption


class ProductImageSerializer(serializers.ModelSerializer):
    """상품 이미지 Serializer"""

    image = serializers.ImageField(use_url=True)

    class Meta:
        model = ProductImage
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    """상품 Serializer"""

    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_image(self, obj):
        """제품 내 모든 이미지 조회"""
        image = obj.productimage_set.all()
        return ProductImageSerializer(
                instance=image, 
                many=True, 
                context=self.context
                ).data

    @transaction.atomic
    def create(self, validated_data):
        """제품 등록"""
        product = Product.objects.create(**validated_data)
        images = self.context['request'].FILES
        
        try:
            """제품 썸네일 저장"""
            for thumbnail in images.getlist("mainImage"):
                ProductImage.objects.create(
                    product=product,
                    image=thumbnail,
                    is_thumbnail=True,
                )

            """제품 상세 저장"""
            for image in images.getlist("image"):
                ProductImage.objects.create(
                    product=product,
                    image=image,
                )
            
            return product

        except KeyError as e:
            transaction.set_rollback(rollback=True)
            raise ValidationError(str(e))

    def update(self, instance, validated_data):
        """제품 수정"""
        images = self.context["request"].FILES
        return super().update(instance, validated_data)