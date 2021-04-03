from django.contrib import admin
from django.urls import path
from django.urls import include
from foodieapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('foodiapp/', include('foodieapp.urls')),
    path('admin/', admin.site.urls),
]
