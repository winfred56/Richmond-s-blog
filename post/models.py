from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images')
    date_posted = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.title