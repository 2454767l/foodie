from django import forms
from django.contrib.auth.models import User
from foodieapp.models import UserProfile

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'password',)
