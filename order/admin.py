from django.contrib import admin
from order.models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display=("order_id","user_name","email","contact","order_date","service","order_status","order_details")
    list_display_links=("order_id","user_name","email")
admin.site.register(Order,OrderAdmin)
