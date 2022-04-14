from django.urls import path

from . import views

# HTTP request -> <- HTTP respons

urlpatterns = [
    path('', views.home),  # Home
    path('recipes/<int:id>/', views.recipe),
]
