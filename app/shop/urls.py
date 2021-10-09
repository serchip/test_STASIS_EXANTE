from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.ProductListView.as_view(), name="ProductList"),
    url(
        r"^(?P<category_slug>[-\w]+)/$",
        views.ProductListView.as_view(),
        name="ProductListByCategory",
    ),
    url(
        r"^(?P<id>\d+)/(?P<slug>[-\w]+)/$",
        views.ProductDetailView.as_view(),
        name="ProductDetail",
    ),
]
