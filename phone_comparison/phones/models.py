from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit
from django.urls import reverse

class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    phone_os = models.CharField(max_length=50)
    phone_ram = models.DecimalField(max_digits=2, decimal_places=0)
    ppi = models.DecimalField(max_digits=3, decimal_places=0)
    dual_camera = models.BooleanField()
    processor = models.CharField(max_length=200)
    screen_resolution = models.CharField(max_length=10)
    radio = models.BooleanField()
    optional = models.TextField(blank=True)

    def __str__(self):
        return self.name
