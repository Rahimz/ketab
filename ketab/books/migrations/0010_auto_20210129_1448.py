# Generated by Django 3.1.5 on 2021-01-29 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20210116_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Illustrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1500)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1500)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='book',
            name='bibliography',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='circulation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='collector',
            field=models.CharField(blank=True, max_length=1500),
        ),
        migrations.AddField(
            model_name='book',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='editor',
            field=models.CharField(blank=True, max_length=1500),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='illustrated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pub_place',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pub_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher_sub_cat',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='re_write',
            field=models.CharField(blank=True, max_length=1500),
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='illustrator',
            field=models.ManyToManyField(blank=True, null=True, related_name='illustrator', to='books.Illustrator'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publisher', to='books.publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publisher2', to='books.publisher'),
        ),
    ]
