from django.db import models

class Pokemon(models.Model):
    '''Покемон.'''
    title = models.CharField('Название покемона', max_length=200)
    photo = models.ImageField('Фото покемона', upload_to='pokemons')
    description = models.CharField('Описание покемона', max_length=2000, null=True, blank=True)
    title_en = models.CharField('Название на английском',  max_length=200, null=True, blank=True)
    title_jp = models.CharField('Название на японском', max_length=200, null=True, blank=True)
    next_evolution = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True,
        verbose_name='В кого покемон эволюционирует',
        blank=True, related_name='+')
    previous_evolution = models.ForeignKey(
        "self", on_delete=models.SET_NULL,
        verbose_name='Из кого покемон эволюционировал',
        null=True, blank=True, related_name='+')
    
    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    '''Покемон на карте.'''
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, verbose_name='Модель покемона',)
    appeared_at = models.DateTimeField('Когда появится покемон', null=True, blank=True)
    disappeared_at = models.DateTimeField('Когда пропадет покемон', null=True, blank=True)
    level = models.IntegerField("Уровень покемона", null=True, blank=True)
    health = models.IntegerField('Здоровье покемона', null=True, blank=True)
    strength = models.IntegerField('Сила покемона', null=True, blank=True)
    defence = models.IntegerField("Защита покемона", null=True, blank=True)
    stamina = models.IntegerField("Выносливость покемона", null=True, blank=True) 

    def __str__(self):
        return f"{self.pokemon}, {self.lat}"
