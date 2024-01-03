# Generated by Django 4.2.7 on 2023-12-11 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("smartcube_api", "0028_cart_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="cart_id",
        ),
        migrations.AlterField(
            model_name="cart",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]