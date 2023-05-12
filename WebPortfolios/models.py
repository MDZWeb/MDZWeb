from django.db import models
import datetime
# Create your models here.
class Webportfolio(models.Model):
    Name=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)
    Url=models.URLField(max_length=250)
    upload_date=models.DateTimeField(default=datetime.datetime.now())
    is_feature=models.BooleanField(default=False)
    Image=models.ImageField(upload_to='Image/WebDesigns')
