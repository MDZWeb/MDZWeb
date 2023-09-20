import django.contrib
from django.db import models
# Create your models here.
class Webdesigns(models.Model):
    website_name=models.CharField(max_length=300)
    url=models.URLField(max_length=600)
    is_feature=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    added_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="Images/WebsiteDesign")

    class Meta:
        verbose_name="Website Design"
        verbose_name_plural="Website Designs"
    
    def __str__(self):
        return self.website_name