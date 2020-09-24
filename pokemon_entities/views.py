import folium
import json
import os

from .models import Pokemon, PokemonEntity
from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned 
MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        pokemon_entitys = PokemonEntity.objects.filter(pokemon__id=pokemon.id)
        for pokemon_entity in pokemon_entitys:
            add_pokemon(
                folium_map, pokemon_entity.lat, pokemon_entity.lon,
                pokemon.title, pokemon.photo.path)

    pokemons_on_page = []
    for pokemon in Pokemon.objects.all():
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.photo.url,
            'title_ru': pokemon.title,
        })


    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        requested_pokemon = Pokemon.objects.get(id=pokemon_id)
    except (MultipleObjectsReturned, ObjectDoesNotExist ):
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')
    
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entitys = PokemonEntity.objects.filter(pokemon__id=requested_pokemon.id)
    for pokemon_entity in pokemon_entitys:
        pokemon = {
            "title_ru": requested_pokemon.title,
            "next_evolution": requested_pokemon.next_evolution,
            "previous_evolution": requested_pokemon.previous_evolution,
            "title_en": requested_pokemon.title_en,
            "title_jp": requested_pokemon.title_jp,
            'img_url': request.build_absolute_uri(requested_pokemon.photo.url),
            'description': requested_pokemon.description
        }
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon['title_ru'], pokemon["img_url"])

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon})
