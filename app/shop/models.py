from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Имя")
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:ProductListByCategory", args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="products",
        verbose_name="Category",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200, db_index=True, verbose_name="product name")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(
        upload_to="products/%Y/%m/%d/", blank=True, verbose_name="image"
    )
    description = models.TextField(blank=True, verbose_name="des")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")
    available = models.BooleanField(default=True, verbose_name="available")
    created = models.DateTimeField(auto_now_add=True, verbose_name="created")
    updated = models.DateTimeField(auto_now=True, verbose_name="updated")

    class Meta:
        ordering = ["name"]
        index_together = [["id", "slug"]]
        verbose_name = "item"
        verbose_name_plural = "item"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:ProductDetail", args=[self.id, self.slug])
