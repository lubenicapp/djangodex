# Generated by Django 4.2.2 on 2023-06-26 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokedex_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=64)),
                ('type_1', models.CharField(max_length=32)),
                ('type_2', models.CharField(max_length=32, null=True)),
                ('total', models.PositiveSmallIntegerField()),
                ('hp', models.PositiveSmallIntegerField()),
                ('attack', models.PositiveSmallIntegerField()),
                ('defense', models.PositiveSmallIntegerField()),
                ('sp_ak', models.PositiveSmallIntegerField()),
                ('sp_def', models.PositiveSmallIntegerField()),
                ('speed', models.PositiveSmallIntegerField()),
                ('generation', models.PositiveSmallIntegerField()),
                ('legendary', models.BooleanField()),
            ],
            options={
                'db_table': 'pokedex_creature',
            },
        ),
    ]
