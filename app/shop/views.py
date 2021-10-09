from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Category, Product


class ProductDetailView(DetailView):
    queryset = Product.objects.filter(available=True)
    template_name = "shop/product/detail.html"
    extra_context = {"cart_product_form": CartAddProductForm()}


class ProductListView(ListView):
    queryset = Product.objects.filter(available=True)
    context_object_name = "products"
    template_name = "shop/product/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = None
        categories = Category.objects.all()
        products = context["object_list"]
        if self.kwargs.get("category_slug"):
            category = get_object_or_404(
                Category, slug=self.kwargs.get("category_slug")
            )
            products = context["object_list"].filter(category=category)
        return {"category": category, "categories": categories, "products": products}
