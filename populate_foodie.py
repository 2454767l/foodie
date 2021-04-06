import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'foodie.settings')

import django
django.setup()
from django.contrib.auth.models import User
from foodieapp.models import Recipe, UserProfile

def populate():
    users = [{'username': 'ben', 'firstname': 'ben',
              'lastname': 'bennison', 'password': '1234'}]

    recipes = [{'title': 'Pizza', 'photo': 'media/pizza.png', 'user': 'ben',
                'description': 'Turn on oven. Put pizza in. Wait 30 mins.',
                'dietPref': 'Vegetarian',
                'ingredients': 'flour, oil, water, tomato sauce, cheese',
                'upvotes': 500},

               {'title': 'Pasta', 'photo': 'media/pasta.jpg', 'user': 'ben',
                'description': 'Boil water. Put pasta in. Wait 10 mins.',
                'dietPref': 'Vegan',
                'ingredients': 'dried pasta', 'upvotes': 20},

               {'title': 'Salad', 'photo': 'media/salad.jpg', 'user': 'ben',
                'description': 'Wash and chop up veg. Toss in a bowl. Serve with vinagrette',
                'dietPref': 'Vegan',
                'ingredients': 'salad, onions, tomatoes, carrots, peppers', 'upvotes': 50}]

    for user in users:
        add_user(user['username'], user['password'])

    for recipe in recipes:
        add_recipe(recipe['title'], recipe['photo'], recipe['user'],recipe['description'], recipe['dietPref'], recipe['ingredients'], recipe['upvotes'])

def add_user(username, password):
    user = User()
    user = User.objects.get_or_create(username=username, password=password)[0]
    user.save()
    user_profile = UserProfile()
    user_profile.user = user
    user_profile.save()

def add_recipe(title, photo, user, description, diet_pref, ingredients, upvotes):
    ##new_recipe = Recipe.objects.get_or_create(title=title, photo=photo, description=description,
                                          ##dietPref=diet_pref, ingredients=ingredients)
    ##un = User.objects.get(username=user)
    ##recipe.user = UserProfile.objects.get(user=un)
    new_recipe = Recipe()
    new_recipe.title = title
    new_recipe.photo = photo
    new_recipe.description = description
    new_recipe.dietPref = diet_pref
    new_recipe.ingredients = ingredients
    new_recipe.upvotes = upvotes
    new_recipe.save()
    
    
# Start execution here!
if __name__ == '__main__':
    print('Starting Foodie population script...')
    populate()
    print('all OK')
