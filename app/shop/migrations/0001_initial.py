# Generated by Django 3.2.7 on 2021-10-09 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: list = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "name",
                    models.CharField(db_index=True, max_length=200, verbose_name="Имя"),
                ),
                ("slug", models.SlugField(max_length=200, unique=True)),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=200, verbose_name="product name"
                    ),
                ),
                ("slug", models.SlugField(max_length=200)),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="products/%Y/%m/%d/", verbose_name="image"
                    ),
                ),
                ("description", models.TextField(blank=True, verbose_name="des")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="price"
                    ),
                ),
                (
                    "available",
                    models.BooleanField(default=True, verbose_name="available"),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="updated"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="shop.category",
                        verbose_name="Category",
                    ),
                ),
            ],
            options={
                "verbose_name": "item",
                "verbose_name_plural": "item",
                "ordering": ["name"],
                "index_together": {("id", "slug")},
            },
        ),
    ]