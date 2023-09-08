from django.shortcuts import render,redirect
from django.http import HttpResponse
#from .forms import TypeSearchForm
from .models import CaughtPokemon
import json
import requests

def determine_winner(pokemon1, pokemon2):
    if pokemon1.level > pokemon2.level:
        return pokemon1.name
    elif pokemon2.level > pokemon1.level:
        return pokemon2.name
    else:
        return "Draw"

        
def battle(request):
    caught_pokemons=CaughtPokemon.objects.all()
    winner=""
    if request.method=='POST':
        pokemon1_name=request.POST.get('pokemon1')
        pokemon2_name=request.POST.get('pokemon2')

        if pokemon1_name and pokemon2_name:
            pokemon1=caught_pokemons.get(name=pokemon1_name)
            pokemon2=caught_pokemons.get(name=pokemon2_name)
            winner = determine_winner(pokemon1, pokemon2)

    context = {'caught_pokemons': caught_pokemons,'winner': winner}
    return render(request, 'pages/battle.html', context)


           
# Create your views here.
