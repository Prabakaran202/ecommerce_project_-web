from rest_framework import serializers
from . models import wishlist
from product.serializers import ProductDetailSerializer

class wishlistSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    product = serializers.CharField(read_only=True)
    
    class Meta:
        model=wishlist
        fields=[
            "id",
            "user",
            "product",
            "quantity",
            "created_date",
            
        ]

class wishlistListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    product = ProductDetailSerializer()
    
    class Meta:
        model=wishlist
        fields=[
            "id",
            "user",
            "product",
            "quantity",
            "created_date", 
        ]
    