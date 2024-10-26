# Generated by Django 5.0.7 on 2024-09-27 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_contact_options_contact_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='title_img',
            field=models.ImageField(blank=True, null=True, upload_to='goods__img', verbose_name='Изображение главного экрана'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='goods__img', verbose_name='Изображение офиса'),
        ),
    ]
