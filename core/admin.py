from django.contrib import admin
from core.models import *

# Register your models here.

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']

    class Meta:
        model = GeneralSetting

@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'file']
    list_editable = ['description', 'file']

    class Meta:
        model = ImageSetting
