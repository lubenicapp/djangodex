from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Pokemon
from pokedex.models import PokedexCreature


@api_view()
def index(request):
    pokemons = Pokemon.objects.all().values()
    return JsonResponse(list(pokemons), safe=False)


@api_view(['POST'])
def create(request):

    try:
        creature = PokedexCreature.objects.get(id=request.data.get('pokedex_creature_id'))
    except PokedexCreature.DoesNotExist:
        return Response({'message': 'Pokedex Creature does not exist'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    pokemon = Pokemon()
    pokemon.pokedex_creature = creature
    pokemon.nickname = request.data.get('nickname')
    pokemon.level = request.data.get('level')
    pokemon.experience = request.data.get('experience')
    pokemon.trainer_id = request.data.get('trainer_id')
    pokemon.save()

    return Response(pokemon.id)
