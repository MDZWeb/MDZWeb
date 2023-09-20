from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User
# Register your models here.

class User_Admin(UserAdmin):
    list_display=("username","email","contact_no","created_date","is_active","is_staff","is_admin","is_superadmin")
    list_display_links=("username","email")
    filter_horizontal=()
    list_filter=()
    fieldsets=()
admin.site.register(User,User_Admin)


