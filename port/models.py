from django.db import models

# Create your models here.
class project(models.Model):
    title=models.TextField(max_length=100)
    discription=models.TextField(max_length=300)
    image=models.ImageField(upload_to='port/images', height_field=None, width_field=None, max_length=None)
    url=models.URLField(blank=True)