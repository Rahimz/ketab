# Generated by Django 3.1.5 on 2021-03-17 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0025_auto_20210211_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='illustrator',
            name='latin_name',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='illustrator',
            name='nationality',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]