# Generated by Django 3.1 on 2020-08-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200812_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default=None, unique=True),
        ),
    ]
