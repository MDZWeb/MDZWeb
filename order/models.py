from django.db import models

# Create your models here.
class Order(models.Model):
    status_v=(("Active","Active"),
                ("Delivered","Delivered"),
                ("In Revision","In Revision"),
                ("Cancelled","Cancelled"),
                ("Completed","Completed"),)
    order_id=models.CharField(max_length=300,blank=True)
    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    user_name=models.CharField(max_length=500)
    email=models.CharField(max_length=600)
    contact=models.CharField(max_length=500)
    order_date=models.DateTimeField(auto_now_add=True)
    service=models.CharField(max_length=500)
    order_status=models.CharField(choices=status_v,max_length=300,default="Active")
    order_details=models.TextField()

    class Meta:
        verbose_name="Order"
        verbose_name_plural="Orders"


    def __str__(self):
        return self.email