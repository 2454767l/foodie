from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.username

class Recipe(models.Model):
    VEGAN = 'VE'
    VEGETARIAN = 'VG'
    DIET_PREFS = [(VEGAN, 'Vegan'), (VEGETARIAN, 'Vegetarian')]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    date = models.DateField
    photo = models.ImageField
    description = models.CharField(max_length=1000)
    dietPref = models.CharField(choices = DIET_PREFS)
    quality = models.IntegerField
    difficulty = models.IntegerField
    

    def __str__(self):
        return self.name

class Rating(models.Model):
    #I think this is allowed? 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    positive = models.BooleanField
    difficulty = models.IntegerField
    date = models.DateField()

class Ingredient(models.Model):
    name = models.CharField(max_length=40, unique=True)
    recipe = models.ManyToManyField(Recipe)