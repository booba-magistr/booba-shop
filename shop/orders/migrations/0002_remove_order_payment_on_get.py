# Generated by Django 5.0.7 on 2024-09-01 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_on_get',
        ),
    ]