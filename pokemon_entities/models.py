from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='pokemons', null=True, blank=True)
    
    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True)
# your models here
