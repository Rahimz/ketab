# Generated by Django 3.1.5 on 2021-01-29 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20210129_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1500)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='illustrator',
            name='name',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=1500),
        ),
        migrations.AddField(
            model_name='book',
            name='translator_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translator_1', to='books.translator'),
        ),
        migrations.AddField(
            model_name='book',
            name='translator_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translator_2', to='books.translator'),
        ),
    ]
