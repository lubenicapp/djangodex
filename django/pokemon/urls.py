from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:pokemon_id>', views.detail),
    path('create', views.create)
]
