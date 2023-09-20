from django.contrib import admin
import django.db
from webdesigns.models import Webdesigns
from django.utils.html import format_html
# Register your models here.

class WebdesignsAdmin(admin.ModelAdmin):
    def Image(self,model):
        return format_html('<img src="{}" width=120 height=120>'.format(model.image.url))

    list_display=("website_name","url","is_feature","is_active","added_date","updated_date","Image")
    list_editable=("is_feature","is_active")
    list_per_page=20


admin.site.register(Webdesigns,WebdesignsAdmin)
