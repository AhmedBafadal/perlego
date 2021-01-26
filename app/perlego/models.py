from django.db import models
from django.contrib.postgres.fields import ArrayField

class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    countries = ArrayField(models.CharField(max_length = 1000, blank=True), default = list)

    
    def __str__(self):
        return f"{self.title}"