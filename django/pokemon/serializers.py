from rest_framework import serializers
from .models import Pokemon


class PokemonSerializer(serializers.Serializer):
    ...
    nickname = serializers.CharField()
    level = serializers.SerializerMethodField(method_name='compute_level')
    wild = serializers.SerializerMethodField(method_name='is_wild')

    def compute_level(self, pokemon: Pokemon):
        return round(pokemon.level + pokemon.experience / 100)

    def is_wild(self, pokemon):
        return pokemon.trainer_id is not None
