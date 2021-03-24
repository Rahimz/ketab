# Generated by Django 3.1.5 on 2021-03-24 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0027_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='address',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='publisher',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
