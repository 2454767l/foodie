from foodieapp.models import Recipe, UserProfile, Rating
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

django.setup()


def populate():
    users = [{'username': 'ben', 'firstname': 'ben',
              'lastname': 'bennison', 'password': '1234'}]

    recipes = [{'title': 'Pizza', 'photo': '', 'user': 'alen',
                'description': 'Turn on oven. Put pizza in. Wait 30 mins.',
                'dietPref': 'Vegetarian', 'difficulty': '2',
                'ingredients': 'flour, oil, water, tomato sauce, cheese'},

               {'title': 'Pasta', 'photo': '', 'user': 'ben',
                'description': 'Boil water. Put pasta in. Wait 10 mins.',
                'dietPref': 'Vegan', 'difficulty': '1',
                'ingredients': 'dried pasta'},

               {'title': 'Salad', 'photo': '', 'user': 'erin',
                'description': 'Wash and chop up veg. Toss in a bowl. Serve with vinagrette',
                'dietPref': 'Vegan', 'difficulty': '1',
                'ingredients': 'salad, onions, tomatoes, carrots, peppers'}]

    ratings = [{'user': 'alen', 'recipe': 'pizza'},
               {'user': 'ben', 'recipe': 'pizza'},
               {'user': 'erin', 'recipe': 'pizza'},
               {'user': 'thomas', 'recipe': 'pizza'},

               {'user': 'alen', 'recipe': 'pasta'},
               {'user': 'ben', 'recipe': 'pasta'},
               {'user': 'erin', 'recipe': 'pasta'},
               {'user': 'thomas', 'recipe': 'pasta '},

               {'user': 'alen', 'recipe': 'salad'},
               {'user': 'ben', 'recipe': 'salad'},
               {'user': 'thomas', 'recipe': 'salad'}
               ]

    for recipe in recipes:
        add_recipe(recipe['title'], recipe['photo'], recipe['user'],
                   recipe['description'], recipe['dietPref'], recipe['difficulty'], recipe['ingredients'])

    for rating in ratings:
        rating_to_add = add_rating(rating['user'], rating['recipe'])


def add_user():
    return None

def add_recipe(title, photo, user, description, dietPref, difficulty, ingredients):
    recipe = Recipe.objects.get_or_create(title=title, photo=photo, user=user, description=description,
                                          dietPref=dietPref, difficulty=difficulty, ingredients=ingredients)
    recipe.user = UserProfile.objects.get(user=user)
    recipe.save()
    return recipe


def add_rating(user, recipe):
    rating = Rating.objects.get_or_create(user=user)
    rating.user = UserProfile.objects.get(user=user)
    rating.recipe = Recipe.objects.get(title=recipe)
    rating.save()
    return rating
