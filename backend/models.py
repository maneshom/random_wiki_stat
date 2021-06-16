from django.db import models
from django.db.models.base import Model

# Create your models here.
class Wiki(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    link = models.URLField()
    no_of_image = models.PositiveSmallIntegerField()
    no_of_link = models.PositiveSmallIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title