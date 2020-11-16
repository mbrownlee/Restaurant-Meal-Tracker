from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=55)
    address = models.CharField(max_length=75)
    