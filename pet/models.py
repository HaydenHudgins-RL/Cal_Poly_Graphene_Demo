from django.db import models
from django.conf import settings


# Defining Event model
class Pet(models.Model):
    name = models.TextField()
    age = models.DecimalField(decimal_places=1, max_digits=5)
