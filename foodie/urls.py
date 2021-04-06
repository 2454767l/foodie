from django.contrib import admin
from django.urls import path
from django.urls import include
from foodieapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('foodieapp/', include('foodieapp.urls', namespace='foodie')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
