# Generated by Django 4.2.7 on 2023-12-06 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("smartcube_api", "0012_cart_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="products",
            field=models.ManyToManyField(
                through="smartcube_api.CartItem", to="smartcube_api.product"
            ),
        ),
    ]