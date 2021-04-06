from foodieapp import views
from django.urls import path

app_name = 'foodieapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('like_recipe/', views.LikeRecipe.as_view(), name='upvote_recipe'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipes/<slug:recipe_title_slug>/', views.show_recipe, name='show_recipe'),
    path('login/account/', views.show_account, name='show_account'),
    path('login/account/newrecipe/', views.new_recipe, name='new_recipe'),
]
