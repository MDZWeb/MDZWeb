from django.contrib import admin
from WebPortfolios.models import Webportfolio
from django.utils.html import format_html
# Register your models here.
class WebportfolioApp(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width=50 height=50>'.format(object.Image.url))
    list_display=('Name','Category','Url','upload_date','is_feature','thumbnail')
    list_display_links=('Name','Category','thumbnail')

admin.site.register(Webportfolio,WebportfolioApp)