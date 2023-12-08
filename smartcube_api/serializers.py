from rest_framework import serializers
from .models import ShopUser, Product, Category, Type, Brand, Cart, CartItem, GiftCard



class ShopUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = ShopUser
        fields = ['id', 'username', 'password', 'email']

    def create(self, validated_data):
        user = ShopUser.objects.create_user(**validated_data)
        return user

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
    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, source='product'
    )

    class Meta:
        model = CartItem
        fields = '__all__'

    def create(self, validated_data):
        # Handle creation of CartItem with product instance
        return CartItem.objects.create(**validated_data)

        
class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = '__all__'
        
class GiftCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftCard
        fields = '__all__'
