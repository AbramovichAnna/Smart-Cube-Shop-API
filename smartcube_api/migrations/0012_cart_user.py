# Generated by Django 4.2.7 on 2023-12-06 22:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("smartcube_api", "0011_rename_date_cart_ctreate_at_remove_cartitem_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cart",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
