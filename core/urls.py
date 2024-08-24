# Import necessary modules
from django.contrib import admin  # Django admin module
from django.urls import path       # URL routing
from authetication.views import *  # Import views from the authentication app
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Static files serving
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
 
# Define URL patterns
urlpatterns = [
    path('', include("authetication.urls")),      # /
    path("admin/", admin.site.urls),          # Admin interface
]

 
# Serve media files if DEBUG is True (development mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()