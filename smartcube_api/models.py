from django.db import models
from django.contrib.auth.models import AbstractUser

# USER
class ShopUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    
    def __str__(self):
        return self.username

# PRODUCT
class Product(models.Model):
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='products_images/')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    info = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)    
    originalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    inStock = models.PositiveIntegerField(default=5)
    ratings = models.DecimalField(max_digits=1, decimal_places=0)

    def __str__(self):
        return self.title
    
# CATEGORIES
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories_images/')

    def __str__(self):
        return self.name
    
# TYPE
class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# BRAND
class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brands_images/')

    def __str__(self):
        return self.name

# CART
class Cart(models.Model):
    cart_id = models.CharField(max_length=100, blank=True,default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cart_id} cart created at {self.created_at}"
    
# CARTITEM
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) 
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.quantity} of {self.product.title}'

# GIFTCARD
class GiftCard(models.Model):
    description = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description

