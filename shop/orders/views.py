from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import CreateOrderForm
from carts.models import Carts
from .models import Order, OrderItem
from django.views.generic import FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CreateOrderView(LoginRequiredMixin, FormView):
    template_name = "orders/orders.html"
    form_class = CreateOrderForm
    success_url = reverse_lazy('order:success_order')

    def get_initial(self):
        initial = super().get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        return initial

    def form_valid(self, form):
        try:
            with transaction.atomic():
                user = self.request.user
                cart_items = Carts.objects.filter(user=user)

                if cart_items.exists():
                    order = Order.objects.create(
                        user=user,
                        phone_number=form.cleaned_data['phone_number'],
                    )

                    for cart_item in cart_items:
                        product=cart_item.product
                        name=cart_item.product.name
                        price=cart_item.product.total_price()
                        quantity=cart_item.quantity


                        if product.count < quantity:
                            raise ValidationError(f'Товар: {name}- нет такого количества. В наличии {product.count}')

                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            name=name,
                            price=price,
                            quantity=quantity,
                        )
                        product.count -= quantity
                        product.save()

                    cart_items.delete()

                    return redirect('order:success_order')
        except ValidationError:
            return redirect('orders:create_order')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оформление'
        context['order'] = True
        return context


class SuccessOrder(TemplateView):
    template_name = "orders/success_order.html"
    extra_context = {"title": "Магазин"}