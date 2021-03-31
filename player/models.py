from django.db import models
from django.conf import settings


# Defining Event model
class Player(models.Model):
    name = models.TextField()
    age = models.DecimalField(decimal_places=1, max_digits=5)
    islands = models.TextField()
    pets = models.TextField()
