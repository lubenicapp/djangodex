# Generated by Django 4.2.2 on 2023-06-26 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_rename_creature_pokedexcreature_pokemon'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pokemon',
        ),
    ]
