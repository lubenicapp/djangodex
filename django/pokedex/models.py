from django.db import models


class Creature(models.Model):
    pokedex_id = models.PositiveIntegerField()
    name = models.CharField(max_length=64)
    type_1 = models.CharField(max_length=32)
    type_2 = models.CharField(max_length=32, null=True)
    total = models.PositiveSmallIntegerField()
    hp = models.PositiveSmallIntegerField()
    attack = models.PositiveSmallIntegerField()
    defense = models.PositiveSmallIntegerField()
    sp_atk = models.PositiveSmallIntegerField()
    sp_def = models.PositiveSmallIntegerField()
    speed = models.PositiveSmallIntegerField()
    generation = models.PositiveSmallIntegerField()
    legendary = models.BooleanField()

    class Meta:
        db_table = 'pokedex_creature'
