from django.db import models


class PokedexCreature(models.Model):
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



class Pokemon(models.Model):
    pokedex_creature_id = models.ForeignKey(PokedexCreature, on_delete=models.CASCADE)
    trainer_id = models.PositiveIntegerField(null=True)
    nickname = models.CharField(max_length=64)
    level = models.PositiveSmallIntegerField(default=1)
    experience = models.PositiveIntegerField(default=0)

    @property
    def is_wild(self):
        return self.trainer_id is None

    def save(self, *args, **kwargs):
        if not self.nickname and self.pokedex_creature_id:
            self.nickname = self.pokedex_creature_id.name
        super().save(*args, **kwargs)
