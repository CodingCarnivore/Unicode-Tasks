from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TypeSearchForm
from .models import CaughtPokemon
import json
import requests

def poketype(request):
    form=TypeSearchForm()
    
    if request.method == 'POST':
        form=TypeSearchForm(request.POST)
        if form.is_valid():
            pokemon_name=form.cleaned_data['type_name']
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/'
            response=requests.get(url)

            if response.status_code==200:
                data=response.json()

                level=data.get('base_experience',0)
                sprite=data['sprites']['front_default'] if 'sprites' in data else ''
                moves=', '.join([move['move']['name'] for move in data.get('moves',[])])
                height=data.get('height',0)/10.0

                caught_pokemon,created= CaughtPokemon.objects.get_or_create(name=pokemon_name) 
                
                if not created:
                    caught_pokemon.level+=1
                else:
                    caught_pokemon.level=level
                caught_pokemon.sprite=sprite
                caught_pokemon.height=height
                caught_pokemon.moves=moves
                caught_pokemon.save()
    context={'form':form,'caught_pokemons':CaughtPokemon.objects.all()}
    return render(request,'pages/poketype.html',context)

           
# Create your views here.
