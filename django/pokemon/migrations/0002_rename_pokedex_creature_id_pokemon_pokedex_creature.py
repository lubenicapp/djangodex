# Generated by Django 4.2.2 on 2023-06-26 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='pokedex_creature_id',
            new_name='pokedex_creature',
        ),
    ]