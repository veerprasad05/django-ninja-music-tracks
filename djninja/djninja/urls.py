from django.contrib import admin
from django.urls import path
# creates a new django-ninja api object
from tracks.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    # define another set of url-parameters prefixed by "api"
    # api object has a urls attribute
    path('api/', api.urls)
]
