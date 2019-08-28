# Generated by Django 2.0.5 on 2019-08-28 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_user_buy_paidcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='', verbose_name='Статья'),
        ),
        migrations.AddField(
            model_name='article',
            name='headline',
            field=models.CharField(default='', max_length=200, verbose_name='Главная полоса'),
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='', upload_to='img/%Y/%m/%d/', verbose_name='ФОТО'),
        ),
        migrations.AddField(
            model_name='article',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Платный контент'),
        ),
    ]
