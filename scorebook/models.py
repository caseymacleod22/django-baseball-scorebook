from django.db import models

# Create your models here.

class Team(models.Model):
    location = models.CharField(max_length=50)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.location