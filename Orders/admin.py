from django.contrib import admin
from Orders.models import Order
# Register your models here.

class OrderApp(admin.ModelAdmin):
    list_display=('First_name','Last_name','Email_id','Contact_no','Service_type','Order_date','Status','order_detail')
    list_display_links=('First_name','Last_name','Email_id')

admin.site.register(Order,OrderApp)
