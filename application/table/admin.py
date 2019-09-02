from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TableFieldSettings, Path


# Register your models here.
class TableFieldSettingsAdmin(admin.ModelAdmin):
    pass


class PathAdmin(admin.ModelAdmin):
    pass


admin.site.register(TableFieldSettings, TableFieldSettingsAdmin)
admin.site.register(Path, PathAdmin)
