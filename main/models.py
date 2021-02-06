from django.db import models

# Create your models here.

class Post(models.Model):
    photo = models.ImageField(upload_to='pics')
    category = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
