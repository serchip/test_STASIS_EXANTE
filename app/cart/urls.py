from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.CartDetailView.as_view(), name="CartDetail"),
    url(
        r"^remove/(?P<product_id>\d+)/$",
        views.CartRemoveView.as_view(),
        name="CartRemove",
    ),
    url(r"^add/(?P<product_id>\d+)/$", views.CartAddView.as_view(), name="CartAdd"),
]
