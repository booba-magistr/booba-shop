# Generated by Django 5.0.7 on 2024-09-02 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_order_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(choices=[(0, 'Обрабатывается'), (1, 'Готов')], default=0),
        ),
    ]
