from django.db import models
from django.contrib.auth.models import User

class MealFav(models.Model):
    name = models.CharField(max_length=55)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    