from rest_framework import serializers
from .models import ShopUser, Product, Category, Type, Brand, Cart, CartItem, GiftCard


#USER
class ShopUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = ShopUser
        fields = ['id', 'username', 'password', 'age', 'city']

    def create(self, validated_data):
        user = ShopUser.objects.create_user(**validated_data)
        return user


#PRODUCT-DETAILS
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    type = TypeSerializer()
    brand = BrandSerializer()
    class Meta:
        model = Product
        fields = '__all__'


#CART
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class GiftCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftCard
        fields = '__all__'
