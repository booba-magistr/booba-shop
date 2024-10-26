from django.db import models

# Create your models here.
class Stuff(models.Model):
    name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, blank=True, null=True,verbose_name='Фамилия')
    slug = models.SlugField(max_length=150, unique=True,verbose_name='Слаг')
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Описание')
    img = models.ImageField(upload_to="goods__img", blank=True, null=True, verbose_name="Изображение")
    phone_number = models.CharField(max_length=20, blank=True, null=True, unique=True, verbose_name='Номер телефона')
    email = models.EmailField(max_length=20, blank=True, null=True, unique=True, verbose_name='email')

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'


class Contact(models.Model):
    name = models.CharField(max_length=64, verbose_name='Имя организации')
    phone_number = models.CharField(max_length=20, blank=True, null=True, unique=True, verbose_name='Номер телефона')
    email = models.EmailField(max_length=20, blank=True, null=True, unique=True, verbose_name='email')
    address = models.CharField(max_length=150, blank=True, verbose_name='Адрес')
    img = models.ImageField(upload_to="goods__img", blank=True, null=True, verbose_name="Изображение офиса")
    title_img = models.ImageField(upload_to="goods__img", blank=True, null=True, verbose_name="Изображение главного экрана")
    
    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'