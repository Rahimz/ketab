# Generated by Django 3.1.5 on 2021-01-15 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210112_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True, verbose_name='Slug'),
        ),
    ]
