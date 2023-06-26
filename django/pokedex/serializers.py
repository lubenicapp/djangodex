from rest_framework import serializers


class CreatureSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    legendary = serializers.BooleanField()
