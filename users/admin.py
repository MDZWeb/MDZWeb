from django.contrib import admin
from users.models import user
# Register your models here.

class user_admin(admin.ModelAdmin):
    list_display=('first_name','last_name','user_name','contact','email','date_joined','last_login','is_staff','is_admin','is_superadmin','is_active')

    list_display_links=('first_name','last_name','user_name','email','contact')
    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(user,user_admin)
