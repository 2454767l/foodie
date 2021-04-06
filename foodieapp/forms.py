from django import forms
from django.contrib.auth.models import User
from foodieapp.models import UserProfile, Recipe, Rating


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'password',)

class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length = 40, help_text="Enter recipe name:")
    photo = forms.ImageField(help_text="Upload image: ", required=False)
    description = forms.CharField(max_length=1000, help_text="Enter description:")
    dietPref = forms.CharField(max_length=1000, help_text="Enter dietary preference:")
    upvotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    difficulty = forms.IntegerField(max_value= 5, min_value=1, help_text="Enter difficulty rating(0-5):")
    ingredients = forms.CharField(max_length=1000, help_text="Enter ingredients list:")

    class Meta:
        model = Recipe
        exclude = ('upvotes', 'date', 'user')