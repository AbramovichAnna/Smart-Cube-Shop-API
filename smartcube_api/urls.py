from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path("users/", views.users, name="users"),
    path("products/", views.products, name="products"),
    path("product/<int:pk>", views.product_details, name="product_details"),
    path("categories/", views.categories, name="categories"),
    path('category/<int:pk>/', views.category, name='category'),
    path("types/", views.types, name="types"),
    path("type/<int:pk>", views.type, name="type"),
    path("brands/", views.brands, name="brands"),
    path("brand/<int:pk>", views.brand, name="brand"),
    path("cart/", views.cart, name="cart"),
    path("add_to_cart/", views.add_to_cart, name="add_to_cart"),
    path("cart_items/", views.cart_items, name="cart_item"),
    # path("orders/", views.orders, name="orders"),
    # path("orders/<int:order_id>", views.order, name="order"),
    path("giftcards/", views.giftcards, name="giftcards"),
    path("giftcard/<int:pk>", views.giftcard, name="giftcard"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("users/", views.users, name="users"),
    path("user/<int:user_id>", views.user, name="user"),
    # path("users/<int:user_id>/cart", views.user_cart, name="user_cart"),
    # path("users/<int:user_id>/orders", views.user_orders, name="user_orders"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
