# Generated by Django 4.2.7 on 2023-12-03 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("smartcube_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="brand",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="smartcube_api.brand"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="smartcube_api.category"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="tag",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="product",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="smartcube_api.type"
            ),
        ),
    ]
