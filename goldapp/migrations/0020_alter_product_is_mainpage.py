# Generated by Django 4.0.2 on 2022-05-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldapp', '0019_alter_product_is_approximate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_mainpage',
            field=models.BooleanField(default=False, verbose_name='Main page'),
        ),
    ]