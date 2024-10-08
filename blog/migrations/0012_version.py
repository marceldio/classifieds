# Generated by Django 4.2 on 2024-08-24 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0011_alter_blog_options_alter_blog_content_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150, verbose_name="Title")),
                ("number", models.PositiveIntegerField(verbose_name="Version number")),
                (
                    "is_current",
                    models.BooleanField(default=False, verbose_name="Is current"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.blog",
                        verbose_name="Post",
                    ),
                ),
            ],
            options={
                "verbose_name": "version",
                "verbose_name_plural": "versions",
            },
        ),
    ]
