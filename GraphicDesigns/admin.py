from django.contrib import admin
from GraphicDesigns.models import GraphicDesign
from django.utils.html import format_html
# Register your models here.
class GraphicDesignAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width=50 height=50>'.format(object.Image.url))

    list_display=('Name','Category','UploadDate','is_feature','thumbnail')
    list_display_links=('Name','Category','thumbnail')

admin.site.register(GraphicDesign,GraphicDesignAdmin)