# Generated by Django 4.2.2 on 2023-06-26 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creature',
            old_name='sp_ak',
            new_name='sp_atk',
        ),
    ]