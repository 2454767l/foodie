from django.contrib import admin
from foodieapp.models import UserProfile, Recipe, Rating
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Recipe)
admin.site.register(Rating)