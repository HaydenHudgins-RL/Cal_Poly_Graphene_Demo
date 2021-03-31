from django.db import models
from django.conf import settings


# Defining Event model
class Island(models.Model):
    name = models.TextField()
    trees = models.TextField()
