# Generated by Django 4.0.2 on 2022-04-03 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldapp', '0013_product_is_concrete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=50, verbose_name='Field')),
            ],
        ),
    ]
