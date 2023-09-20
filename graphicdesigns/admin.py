from django.contrib import admin
from graphicdesigns.models import Graphic_Designs
from django.utils.html import format_html
# Register your models here.

class GraphicDesignAdmin(admin.ModelAdmin):
    def Image(self,model):
        return format_html('<img src="{}" width=120 height=120>'.format(model.image.url))
    list_display=("design_name","design_type","is_feature","is_active","added_date","updated_date","Image")
    list_editable=("is_feature","is_active")
    list_per_page=10

admin.site.register(Graphic_Designs,GraphicDesignAdmin)
