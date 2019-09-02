from django.db import models

# Create your models here.
from django.shortcuts import render
from django.db import models


# from phones.models import

class TableFieldSettings(models.Model):
    title = models.CharField(max_length=50)
    width = models.IntegerField()
    index = models.IntegerField()

    def __str__(self):
        return f'{self.title}'


class Path(models.Model):
    path = models.FilePathField()

    @property
    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path

    def __str__(self):
        return f'{self.path}'
