# Generated by Django 4.0.2 on 2022-05-26 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goldapp', '0026_product_name_az_product_name_en'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name_az',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_en',
        ),
    ]