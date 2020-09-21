from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='pokemons', null=True, blank=True)
    
    def __str__(self):
        return f"{self.title}"


# your models here
