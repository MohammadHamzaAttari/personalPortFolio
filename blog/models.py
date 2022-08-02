from time import timezone
from django.db import models

class Blog(models.Model):
    heading=models.TextField(max_length=100)
    description=models.TextField(max_length=700)
    date=models.DateField(timezone)
