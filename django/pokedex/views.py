from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PokedexCreature
from .serializers import CreatureSerializer


@api_view()
def index(request):
    """
        List of all Pokédex Creatures internal data attributes
    """
    custom_filter = filter_on_attributes({'type_1', 'type_2', 'legendary'}, request)
    creatures = PokedexCreature.objects.all()
    creatures = creatures.filter(**custom_filter)

    data = [model_to_dict(creature) for creature in creatures]

    return JsonResponse(data, safe=False)


@api_view()
def detail(request, creature_id):
    """
        Detail view of a Pokédex Creature with API attributes
    """
    creature = PokedexCreature.objects.get(pk=creature_id)
    serializer = CreatureSerializer(creature)
    return Response(serializer.data)



def filter_on_attributes(attribute_set: set, request) -> dict:
    """
        filter helper.
        builds a dictionary with the query parameters if provided
    """
    return {k: request.GET.get(k) for k in attribute_set if request.GET.get(k) is not None}
