# Generated by Django 4.0.2 on 2022-05-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldapp', '0017_newmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Newmodel',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='is_concrete',
            new_name='is_approximate',
        ),
        migrations.AddField(
            model_name='product',
            name='is_mainpage',
            field=models.BooleanField(default=False, verbose_name='Mainpage'),
        ),
    ]
