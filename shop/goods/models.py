from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=150, unique=True, blank=True, null=True, verbose_name="Слаг"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    slug = models.SlugField(
        max_length=150, unique=True, blank=True, null=True, verbose_name="Слаг"
    )
    img = models.ImageField(
        upload_to="goods__img", blank=True, null=True, verbose_name="Изображение"
    )
    description = models.TextField(
        max_length=1000, blank=True, null=True, verbose_name="Описание"
    )
    price = models.DecimalField(
        default=0.00, max_digits=8, decimal_places=2, verbose_name="Цена"
    )
    discount = models.IntegerField(blank=True, verbose_name="Скидка", null=True)
    count = models.PositiveIntegerField(default=0, verbose_name="Количество")
    cat = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Категория",
        related_name="products",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self) -> str:
        return self.name

    def total_price(self):
        if self.discount:
            return self.price - self.price * self.discount / 100
        return self.price

    def get_absolute_url(self):
        return reverse("goods:product", kwargs={"product_slug": self.slug})


# class City(models.Model):
#     name = models.SlugField(max_length=100, unique=True, verbose_name="Имя города")
#     slug = models.SlugField(
#         max_length=150, unique=True, blank=True, null=True, verbose_name="Слаг"
#     )
