# Generated by Django 2.0.5 on 2019-08-06 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Имя')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('image', models.CharField(max_length=128, verbose_name='Изображение')),
                ('release_date', models.DateField(verbose_name='Дата релиза')),
                ('lte_exists', models.BooleanField(verbose_name='LTE')),
                ('slug', models.CharField(max_length=70)),
            ],
        ),
    ]