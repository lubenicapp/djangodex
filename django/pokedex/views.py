from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Creature
from .serializers import CreatureSerializer


@api_view()
def index(request):
    creatures = Creature.objects.all()
    return Response(creatures)


@api_view()
def detail(request, creature_id):
    creature = Creature.objects.get(pk=creature_id)
    serializer = CreatureSerializer(creature)
    return Response(serializer.data)
