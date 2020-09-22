from django.db import models

class Pokemon(models.Model):
    '''Покемон.'''
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='pokemons')
    description = models.CharField(max_length=2000, null=True, blank=True)
    title_en = models.CharField(max_length=200, null=True, blank=True)
    title_jp = models.CharField(max_length=200, null=True, blank=True)
    next_evolution = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True,
        blank=True, related_name='+')
    previous_evolution = models.ForeignKey(
        "self", on_delete=models.SET_NULL,
        null=True, blank=True, related_name='+')
    
    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    '''Покемон на карте.'''
    lat = models.FloatField()
    lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True) 

    def __str__(self):
        return f"{self.pokemon}, {self.lat}"
# your models here
