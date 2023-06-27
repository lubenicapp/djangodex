from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:pokemon_id>', views.detail),
    path('<int:pokemon_id>/give-xp', views.give_xp),
    path('create', views.create),
]
