from django.contrib.admin import ModelAdmin, register
from api.models import File, Folder
# Register your models here.

@register(Folder)
class FolderAdmin(ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    search_fields = ['name']

@register(File)
class FileAdmin(ModelAdmin):
    list_display = ['id', 'name','folder', 'created_at', 'file']
    search_fields = ['name', 'folder']
    autocomplete_fields = ['folder']