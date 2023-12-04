from django.contrib import admin
from .models import Product, Category, CartItem, Brand, Type, GiftCard, Cart, Order, ShopUser


admin.site.register(ShopUser)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Brand)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(GiftCard)


