from tabnanny import verbose
from django.db import models
from users.models import User
from goods.models import Product


# Create your models here.
class CartQueryset(models.QuerySet):
    def total_goods_price(self):
        return sum(cart.product.total_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Carts(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Пользователь",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
    )
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Время добавления"
    )
    session_key = models.CharField(max_length=32, blank=True, null=True)

    objects = CartQueryset().as_manager()

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        if self.user:
            return f"Пользователь {self.user.username} {self.product.name} {self.quantity}"
        return f"Анонимный пользователь {self.product.name} {self.quantity}"

    def product_price(self):
        if self.quantity:
            return round(self.product.total_price() * self.quantity, 2)
        return self.product.total_price()
