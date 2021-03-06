# Generated by Django 2.2.3 on 2020-09-22 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='Defence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='Health',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='Stamina',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='Strength',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
