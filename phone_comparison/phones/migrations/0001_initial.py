# Generated by Django 2.0.5 on 2019-08-06 18:15

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
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('phone_os', models.CharField(max_length=50)),
                ('phone_ram', models.DecimalField(decimal_places=0, max_digits=2)),
                ('ppi', models.DecimalField(decimal_places=0, max_digits=3)),
                ('dual_camera', models.BooleanField()),
                ('processor', models.CharField(max_length=200)),
                ('screen_resolution', models.CharField(max_length=10)),
                ('radio', models.BooleanField()),
                ('optional', models.TextField()),
            ],
        ),
    ]