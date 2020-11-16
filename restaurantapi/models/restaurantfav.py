from django.db import models
from django.contrib.auth.models import User

class RestaurantFav(models.Model):
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    