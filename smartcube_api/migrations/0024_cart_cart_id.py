# Generated by Django 4.2.7 on 2023-12-08 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("smartcube_api", "0023_rename_customer_shopuser_remove_cart_products"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="cart_id",
            field=models.CharField(blank=True, default=1, max_length=100),
        ),
    ]
