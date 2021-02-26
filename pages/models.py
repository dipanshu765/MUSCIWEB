from django.db import models
from datetime import datetime
# Create your models here.

class Song(models.Model):
    title= models.CharField(max_length=20)
    audio= models.FileField(upload_to="music")
    theme= models.ImageField(upload_to="%d%m%y")
    post_date= models.DateTimeField(default=datetime.now())
    singer= models.CharField(max_length=50)
    description= models.TextField(max_length=200)
    def __str__(self):
        return self.title

