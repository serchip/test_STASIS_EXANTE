from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Order, OrderItem


def OrderDetail(obj):
    return format_html(
        '<a href="{}">Посмотреть</a>'.format(
            reverse("orders:AdminOrderDetail", args=[obj.id])
        )
    )


OrderDetail.short_description = "Инфо"  # type: ignore


def owner_email(obj):
    return obj.owner.email


owner_email.short_description = "email"  # type: ignore


def owner_first_name(obj):
    return obj.owner.first_name


owner_first_name.short_description = "first_name"  # type: ignore


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ["product"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", owner_first_name, owner_email, "created", OrderDetail]
    list_filter = ["created", "updated"]
    search_fields = ("=id", "owner__email")
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
