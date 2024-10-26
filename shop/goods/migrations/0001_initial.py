# Generated by Django 5.0.7 on 2024-08-12 08:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=150, null=True, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=150, null=True, unique=True, verbose_name='Слаг')),
                ('img', models.ImageField(blank=True, null=True, upload_to='goods__img', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Цена')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='Скидка')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='goods.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
