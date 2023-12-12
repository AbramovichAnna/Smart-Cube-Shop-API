# Generated by Django 4.2.7 on 2023-12-11 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("smartcube_api", "0030_cartitem_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="user",
        ),
        migrations.RemoveField(
            model_name="cartitem",
            name="user",
        ),
        migrations.AddField(
            model_name="cart",
            name="cart_id",
            field=models.CharField(blank=True, default=1, max_length=100),
        ),
    ]
