from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import RedirectView, TemplateView, View
from shop.models import Product

from .cart import Cart
from .forms import CartAddProductForm


class CartAddView(View):
    form_class = CartAddProductForm

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = kwargs["product_id"]
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(
                product=product, quantity=cd["quantity"], update_quantity=cd["update"]
            )
        return redirect("cart:CartDetail")


class CartRemoveView(RedirectView):
    pattern_name = "cart:CartDetail"

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id=kwargs["product_id"])
        cart.remove(product)
        return super().get(request)


class CartDetailView(TemplateView):
    template_name = "cart/detail.html"

    def get_context_data(self):
        cart = Cart(self.request)
        for item in cart:
            item["update_quantity_form"] = CartAddProductForm(
                initial={"quantity": item["quantity"], "update": True}
            )

        return super().get_context_data(**{"cart": cart})
