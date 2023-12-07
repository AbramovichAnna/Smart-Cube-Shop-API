# Generated by Django 4.2.7 on 2023-12-07 16:58

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("smartcube_api", "0015_remove_cartitem_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cart",
            old_name="ctreate_at",
            new_name="ctreated_at",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="products",
        ),
        migrations.AddField(
            model_name="cartitem",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="shopuser",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
        migrations.AlterField(
            model_name="shopuser",
            name="username",
            field=models.CharField(
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=150,
                unique=True,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="username",
            ),
        ),
    ]
