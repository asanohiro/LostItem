# photos/models.py
from django.db import models

class LostItem(models.Model):
    image = models.ImageField(upload_to='lost_items/')
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


