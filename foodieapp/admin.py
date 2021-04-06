from django.contrib import admin
from foodieapp.models import UserProfile, Recipe
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(UserProfile)
admin.site.register(Recipe, RecipeAdmin)
