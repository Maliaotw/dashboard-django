from django.contrib import admin

from . import models

admin.site.register(models.Department)
admin.site.register(models.Category)


@admin.register(models.Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = [
        'number',
        'category',
        'department',
        'remarks'
    ]

