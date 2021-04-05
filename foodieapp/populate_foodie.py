from foodieapp.models import Recipe, UserProfile, Rating
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

django.setup()

def populate():
    # create users from dictionaries,
    # then create recipes linked to them,
    # then create ratings
    users = [{'username':'ben', 'firstname':'ben', 'lastname':'bennison', 'password':'1234' }]

    recipes = [{'title': 'Pizza', 'photo': '',
                'description': 'Turn on oven. Put pizza in. Wait 30 mins.',
                'dietPref': 'Vegetarian', 'difficulty': '2', 
                'ingredients': 'flour, oil, water, tomato sauce, cheese'},
                {'title': 'Pasta', 'photo': '',

                'description': 'Boil water. Put pasta in. Wait 10 mins.',
                'dietPref': 'Vegan', 'difficulty': '1', 
                'ingredients': 'dried pasta'},

                {'title': 'Salad', 'photo': '',
                'description': 'Wash and chop up veg. Toss in a bowl. Serve with vinagrette',
                'dietPref': 'Vegan', 'difficulty': '1', 
                'ingredients': 'salad, onions, tomatoes, carrots, peppers'}]

    ratings = [{'user':'alen', 'recipe':'pizza'},
                {'user':'ben', 'recipe':'pizza'}, 
                {'user':'erin', 'recipe':'pizza'},
                {'user':'thomas', 'recipe':'pizza'},

                {'user':'alen', 'recipe':'pasta'},
                {'user':'ben', 'recipe':'pasta'}, 
                {'user':'erin', 'recipe':'pasta'},
                {'user':'thomas', 'recipe':'pasta '},

                {'user':'alen', 'recipe':'salad'},
                {'user':'ben', 'recipe':'salad'},
                {'user':'thomas', 'recipe':'salad'}
                ]

    


    