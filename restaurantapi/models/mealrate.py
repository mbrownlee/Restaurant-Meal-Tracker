from django.db import models
from django.contrib.auth.models import User

class MealRate(models.Model): 
    meal = models.ForeignKey("Meal", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField ()
