# Generated by Django 3.1 on 2020-08-23 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='produts',
            new_name='products',
        ),
    ]
