from django.db import models
import datetime

# Create your models here.

category_type=[
    ('Social Media Design','Social Media Design'),
    ('Face Book Covers','Face Book Covers'),
    ('Flyer Design','Flyer Design'),
    ('Business Card Design','Business Card Design'),
]

class GraphicDesign(models.Model):
    Name=models.CharField(max_length=100)
    Category=models.CharField(max_length=100,choices=category_type,default='Social Media Design')
    UploadDate=models.DateTimeField(default=datetime.datetime.now())
    is_feature=models.BooleanField(default=False)
    Image=models.ImageField(upload_to='Image/Graphic Designs')

