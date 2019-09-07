from django.db import models
from django.conf import settings


class Table(models.Model):
    ordinal_column = models.IntegerField(primary_key=True)
    name_column = models.CharField(max_length=50)
    width_column = models.IntegerField(default=1)

    def __str__(self):
        return self.name_column


class FilePath(models.Model):
    file_obj = models.FilePathField(path=settings.BASE_DIR)

    @property
    def get_path(self):
        return self.file_obj

    def set_path(self, file_obj):
        self.file_obj = file_obj

    def __str__(self):
        return self.file_obj
