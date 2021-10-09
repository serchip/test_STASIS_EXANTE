from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^create/$", views.OrderCreateView.as_view(), name="OrderCreate"),
    url(
        r"^admin/order/(?P<order_id>\d+)/$",
        views.AdminOrderDetail,
        name="AdminOrderDetail",
    ),
]
