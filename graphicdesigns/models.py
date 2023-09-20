from django.db import models

# Create your models here.
class Graphic_Designs(models.Model):
    design_type=(("Social Media Design","Social Media Design"),
                ("Face Book Covers","Face Book Covers"),
                ("Flyer Design","Flyer Design"),
                ("Business Card Design","Business Card Design"),)

    design_name=models.CharField(max_length=300)
    design_type=models.CharField(choices=design_type,max_length=300,default="Social Media Design")
    is_feature=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    added_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="Images/GraphicDesign")

    class Meta:
        verbose_name="Graphic Design"
        verbose_name_plural="Graphic Designs"
    
    def __str__(self):
        return self.design_name