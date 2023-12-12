# Generated by Django 4.2.7 on 2023-12-08 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("admin", "0003_logentry_add_action_flag_choices"),
        ("smartcube_api", "0022_rename_shopuser_customer_cart_products"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Customer",
            new_name="ShopUser",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="products",
        ),
    ]
