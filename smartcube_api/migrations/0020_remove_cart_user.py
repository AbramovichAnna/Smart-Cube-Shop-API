# Generated by Django 4.2.7 on 2023-12-07 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("smartcube_api", "0019_cart_updated_at_alter_cart_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="user",
        ),
    ]
