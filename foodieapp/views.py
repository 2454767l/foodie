from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from foodieapp.models import UserProfile, Recipe
from foodieapp.forms import UserForm, RecipeForm
from django.views.generic import View


def home(request):
    highest_voted = Recipe.objects.order_by('upvotes')[:5]
    context_dict = {}
    context_dict['highest'] = highest_voted
    return render(request, 'foodie/home.html', context=context_dict)


def search(request):
    query = request.GET.get('query')
    query_filter = request.GET.get('filter')
    
    if query_filter == "title":
        results = Recipe.objects.filter(title=query)
    elif query_filter == "user":    
        current = UserProfile.objects.get(user=request.user)
        results = Recipe.objects.filter(user=current)
    elif query_filter == "ingredients":
        results = Recipe.objects.filter(ingredients__contains=query)
    
    context_dict = {}
    context_dict['recipes'] = results
    return render(request, 'foodie/search.html', context=context_dict)

def recipes(request):
    all_recipes = Recipe.objects
    context_dict= {}
    context_dict['all'] = all_recipes

    return render(request, 'foodie/allRecipes.html', context=context_dict)


def show_recipe(request, recipe_title_slug):
    context_dict = {}

    try:
        recipe = Recipe.objects.get(slug=recipe_title_slug)
        context_dict['recipe'] = recipe
    except Recipe.DoesNotExist:
        context_dict['recipe'] = None

    return render(request, 'foodie/recipe.html', context=context_dict)

@login_required
def new_recipe(request):
    current = UserProfile.objects.get(user=request.user)
    recipe = Recipe()
    
    if request.method=='POST':
        recipe_form = RecipeForm(request.POST)

        if recipe_form.is_valid:
            recipe = recipe_form.save(commit=False)
            recipe.user = current
            recipe.save()
            return redirect(reverse('foodie:home'))
        else:
            print(form.errors)
    else:
            recipe_form = RecipeForm()


    return render(request, 'foodie/newrecipe.html', context={'form':recipe_form})

@login_required
def show_account(request):
    current = UserProfile.objects.get(user=request.user)
    user_recipes = Recipe.objects.filter(user=current)
    context_dict = {}
    context_dict['recipes'] = user_recipes
    return render(request, 'foodie/myAccount.html', context=context_dict)

    

def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            user_profile = UserProfile()
            user = user_form.save()
            user.set_password(user.password)
            user_profile.user = user
            user.save()
            user_profile.user = user
            user_profile.save()
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


