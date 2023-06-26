from django.db import models
from pokedex.models import PokedexCreature


# Create your models here.
class Pokemon(models.Model):
    pokedex_creature = models.ForeignKey(PokedexCreature, on_delete=models.CASCADE)
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
