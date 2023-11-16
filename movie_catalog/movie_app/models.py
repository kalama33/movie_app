from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_lenght=100)
    genre = models.CharField(max_lenght=100)
    year = model.IntegerField()
    director = models.CharField(max_lenght=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
