from django.db import models
import datetime
# Create your models here.
class Order(models.Model):
    services_category=(
        ("Website","Website"),
        ("Graphic Design","Graphic Design"),
    )

    status_cat=(
        ("Active","Active"),
        ("Delivered","Delivered"),
        ("Revision","Revision"),
        ("Completed","Completed"),
    )

    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Email_id=models.EmailField(max_length=200)
    Contact_no=models.CharField(max_length=100)
    Service_type=models.CharField(choices=services_category,default="Website")
    Order_date=models.DateTimeField(default=datetime.datetime.now())
    Status=models.CharField(choices=status_cat,max_length=100,default="Active")
    order_detail=models.TextField()

