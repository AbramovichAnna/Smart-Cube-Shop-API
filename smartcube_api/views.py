from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import ShopUser, Product, Category, CartItem, Brand, Type, GiftCard, Cart
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ShopUserSerializer, ProductSerializer, GiftCardSerializer, CartSerializer, CategorySerializer, CartItemSerializer, BrandSerializer, TypeSerializer, CartSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser

def index(request):
    return HttpResponse("""<h1>SpeedCube shop API</h1>
                            <p>API for a shop application</p>
                            <p>Available endpoints:</p>
                            <ul>
                                <li>All users :         <a href="/users/">/users/</a></li>
                                <li>All Products :      <a href="/products/">/products/</a></li>
                                <li>Single Product :    <a href="/product/1">/product/1/</a></li>
                                <li>All Categories :    <a href="/categories/">/categories/</a></li>
                                <li>Single Category :   <a href="/category/1">/category/1/</a></li>
                                <li>All Types :         <a href="/types/">/types/</a></li>
                                <li>Single Type :       <a href="/type/1">/type/1/</a></li>
                                <li>All Brands :        <a href="/brands/">/brands/</a></li>
                                <li>Single Brand :      <a href="/brand/4">/brand/4/</a></li>
                                <li>All Gigtcards :     <a href="/giftcards/">/giftcards/</a></li>
                                <li>Single Giftcard :   <a href="/giftcard/1">/giftcard/1/</a></li>
                                <li>Cart :              <a href="/cart/">/cart/</a></li>
                                <li>Cart Items :        <a href="/cart_items">/cart_items</a></li>
                            </ul>
                        """)

#USERS
@api_view()
def users(request):
    all_users = ShopUserSerializer(ShopUser.objects.all(), many=True).data
    return Response(all_users)

# PRODUCTS
@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        search_query = request.GET.get('search', '')
        category = request.GET.get('category', '')
        if search_query:
            products = products.filter(title__icontains=search_query)
        all_products = ProductSerializer(products, many=True).data
        return Response(all_products)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

# PRODUCT DETAILS
@api_view(['GET', 'PUT', 'DELETE'])
def product_details(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# CATEGORIES
@api_view()
def categories(request):
    all_categories = CategorySerializer(Category.objects.all(), many=True).data
    return Response(all_categories)

    
# CATEGORY
@api_view(['GET'])
def category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category)
    return Response(serializer.data)


# TYPES
@api_view()
def types(request):
    if request.method == 'GET':
        types = Type.objects.all()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data)
    
# TYPE
@api_view()
def type(request, pk):
    try:
        type = Type.objects.get(pk=pk)
    except Type.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TypeSerializer(type)
        return Response(serializer.data)

# BRANDS
@api_view()
def brands(request):
    brands = BrandSerializer(Brand.objects.all(), many=True).data
    return Response(brands)

# BRAND
@api_view()
def brand(request, pk):
    try:
        brand = Brand.objects.get(pk=pk)
    except Brand.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BrandSerializer(brand)
        return Response(serializer.data)

# CATEGORIES
@api_view()
def categories(request):
    all_categories = CategorySerializer(Category.objects.all(), many=True).data
    return Response(all_categories)

    
# CATEGORY
@api_view(['GET'])
def category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category)
    return Response(serializer.data)

# TYPES
@api_view()
def types(request):
    if request.method == 'GET':
        types = Type.objects.all()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data)
    
# TYPE
@api_view()
def type(request, pk):
    try:
        type = Type.objects.get(pk=pk)
    except Type.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TypeSerializer(type)
        return Response(serializer.data)

# BRANDS
@api_view()
def brands(request):
    all_brands = BrandSerializer(Brand.objects.all(), many=True).data
    return Response(all_brands)

# BRAND
@api_view()
def brand(request, pk):
    try:
        brand = Brand.objects.get(pk=pk)
    except Brand.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BrandSerializer(brand)
        return Response(serializer.data)

# GIFTCARDS
@api_view(['GET', 'POST'])
def giftcards(request):
    if request.method == 'GET':
        gift_cards = GiftCard.objects.all()
        serializer = GiftCardSerializer(gift_cards, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GiftCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
# GIFTCARD
@api_view(['GET', 'PUT', 'DELETE'])
def giftcard(request, pk):
    try:
        giftcard = GiftCard.objects.get(pk=pk)
    except GiftCard.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = GiftCardSerializer(giftcard)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = GiftCardSerializer(giftcard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        giftcard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# CART
@api_view(['GET', 'PUT', 'DELETE'])
def cart(request):
    if request.method == 'GET':
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# CART ITEM
@api_view(['GET', 'POST'])
def cart_items(request):
    if request.method == 'GET':
        all_cart_items = CartItem.objects.all()
        serializer = CartItemSerializer(all_cart_items, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        cart_id = request.session.get('cart_id')
        if not cart_id:
            # Create a new Cart and save its ID in the session
            new_cart = Cart.objects.create()
            request.session['cart_id'] = new_cart.id
            cart_id = new_cart.id
        request.data['cart'] = cart_id
        cart_item_serializer = CartItemSerializer(data=request.data)
        if cart_item_serializer.is_valid():
            cart_item_serializer.save()
            return Response(cart_item_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(cart_item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def update_cart_items(request, pk):
    try:
        cart_item = CartItem.objects.get(pk=pk)
    except CartItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)
    elif request.method == 'PUT':
        quantity = request.data.get('quantity')
        if quantity == 0:
            cart_item.delete()
            return Response(CartItemSerializer(CartItem.objects.all(), many=True).data)
        elif quantity > cart_item.product.inStock:
            return Response({"error": "Quantity exceeds stock"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            cart_item.quantity = quantity
            cart_item.save()
            return Response(CartItemSerializer(CartItem.objects.all(), many=True).data)
    elif request.method == 'DELETE':
        cart_item.delete()
        return Response(CartItemSerializer(CartItem.objects.all(), many=True).data)
    
# USER REGISTER
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = ShopUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Method not allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
# HERO PRODUCTS
@api_view(['GET'])
def hero_products(request):
    hero_products = Product.objects.filter(tag='hero-product')
    serializer = ProductSerializer(hero_products, many=True)
    return Response(serializer.data)
