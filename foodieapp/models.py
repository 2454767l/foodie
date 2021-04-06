from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Recipe(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=40)
    date = models.DateField(default=datetime.now)
    photo = models.ImageField(upload_to='user_images', blank=True)
    description = models.CharField(max_length=1000)
    dietPref = models.CharField(max_length=100)
    upvotes = models.IntegerField
    ingredients = models.CharField(max_length=1000)
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = 'recipes'

    def __str__(self):
        return self.title


