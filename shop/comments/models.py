from django.db import models
from users.models import User
from django.utils import timezone


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    review = models.TextField(max_length=200, verbose_name='Отзыв')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'