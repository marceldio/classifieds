# Generated by Django 4.2 on 2024-08-24 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "catalog",
            "0030_alter_product_created_at_alter_product_is_published_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(default="Ad", max_length=100, verbose_name="name"),
        ),
    ]
