from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from foodieapp.models import UserProfile
from foodieapp.forms import UserForm

def home(request):
    return render(request, 'foodie/home.html')
    
def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    
    return render(request, 'foodie/register.html', context = {'user_form': user_form,
                                                            'registered': registered})

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('foodie:home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
            
    else:
        return render(request, 'foodie/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('foodie:home'))

class LikeRecipe(View):
    def get(self, request):
        recipe_id = request.GET['recipe.id']
        recipe = recipe.objects.get(id = int(recipe_id))
        recipe.upvotes += 1
        recipe.save()

        return HttpResponse(recipe.upvotes)


