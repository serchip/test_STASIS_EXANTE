#!/usr/bin/python
# - *- coding: utf- 8 - *-

from decimal import Decimal

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from shop.models import Product


class Order(models.Model):
    # first_name = models.CharField(verbose_name='Имя', max_length=50)
    # last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    # email = models.EmailField(verbose_name='Email')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)
    discount = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        ordering = ("-created",)
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return "Заказ: {}".format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal("100"))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=1)

    def __str__(self):
        return "{}".format(self.id)

    def get_cost(self):
        return self.price * self.quantity
