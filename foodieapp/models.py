from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Recipe(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=40)
    date = models.DateField(default=datetime.now)
    photo = models.ImageField(upload_to='user_images', blank=True)
    description = models.CharField(max_length=1000)
    dietPref = models.CharField(max_length=100)
    upvotes = models.IntegerField
    difficulty = models.IntegerField
    ingredients = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.title


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    positive = models.BooleanField
    difficulty = models.IntegerField
    date = models.DateField()

