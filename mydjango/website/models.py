from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
