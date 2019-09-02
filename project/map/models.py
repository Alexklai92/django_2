from django.db import models

# Create your models here.
from django.db import models

class Route(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name}'

class Station(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=150)
    routes = models.ManyToManyField(Route, related_name="stations")

    def __str__(self):
        return f'{self.name}'
