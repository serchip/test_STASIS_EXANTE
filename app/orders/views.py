import random
import string
from typing import Any, Dict

from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import FormView

from .forms import OrderCreateForm
from .models import Order, OrderItem

random_str = lambda N: "".join(  # noqa: E731
    random.SystemRandom().choice(
        string.ascii_uppercase + string.ascii_lowercase + string.digits
    )
    for _ in range(N)
)


class OrderCreateView(FormView):
    form_class = OrderCreateForm
    template_name = "orders/order/create.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        kwargs["cart"] = Cart(self.request)
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        username: str = ""
        password: str = ""
        cart = Cart(request)
        form = self.get_form()
        if not request.user.is_authenticated:
            form = self.get_form()
            if form.is_valid():
                username = random_str(15)
                while User.objects.filter(username=username).exists():
                    username = random_str(15)
                owner, is_create = User.objects.get_or_create(
                    email=form.cleaned_data["email"],
                    defaults={
                        "first_name": form.cleaned_data["first_name"],
                        "username": username,
                        "is_staff": True,
                    },
                )
                if is_create:
                    password = User.objects.make_random_password()
                    owner.set_password(password)
                    owner.save(update_fields=["password"])
            else:
                return self.form_invalid(form)
        else:
            owner = request.user
        order = Order.objects.create(owner=owner)
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item["product"],
                price=item["price"],
                quantity=item["quantity"],
            )
        cart.clear()

        request.session["order_id"] = order.id
        self.template_name = "orders/order/created.html"
        return self.render_to_response(
            self.get_context_data(
                **{"order": order, "password": password, "username": username}
            )
        )


@staff_member_required
def AdminOrderDetail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "admin/orders/order/detail.html", {"order": order})
