from django.urls import path

from recipes.views import home

# HTTP request -> <- HTTP respons

urlpatterns = [
    path('', home),  # Home
]
