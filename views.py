from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TypeSearchForm
from .models import CaughtPokemon
import json
import requests

"""
def index(request):
    response=requests.get("https://pokeapi.co/api/v2/type/")
    data=response.json()
    types=[]
    for i in data["results"]:
        types.append(i["name"])

    context={"types":types}
    return render(request, 'pages/index.html',context)
"""
"""
def pokeshow(request):
    form=TypeSearchForm()
    pokemons=[]

    if request.method == 'POST':
        form=TypeSearchForm(request.POST)#creates a form instance and populates it with data from the request
        if form.is_valid():
            type_name=form.cleaned_data['type_name']#cleaned data means the data is normalized in a dictionary format
            url = f'https://pokeapi.co/api/v2/type/{type_name.lower()}/'#user may enter in caps
            response=requests.get(url)
            data=response.json()
            pokemons=[entry['pokemon']['name'] for entry in data['pokemon']]
            
   
    context={'form':form,'pokemons':pokemons}
    return render(request,'pages/pokeshow.html',context)
"""

def poketype(request):
    form=TypeSearchForm()
    pokemons=[] # a list which holds all instances of the pokemons searched

    if request.method == 'POST':
        form=TypeSearchForm(request.POST)#creates a form instance and populates it with data from the request
        if form.is_valid():
            pokemon_name=form.cleaned_data['type_name']#cleaned data means the data is normalized in a dictionary format
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/'#user may enter in caps
            response=requests.get(url)

            if response.status_code==200:
                data=response.json()

                #level=data.get('base_experience',0)
                sprite=data['sprites']['front_default'] if 'sprites' in data else ''
                moves=', '.join([move['move']['name'] for move in data.get('moves',[])])
                height=data.get('height',0)/10.0

                caught_pokemon,created= CaughtPokemon.objects.get_or_create(name=pokemon_name.lower()) 
                caught_pokemon.level+=1
                caught_pokemon.sprite=sprite
                caught_pokemon.height=height
                caught_pokemon.moves=moves
                caught_pokemon.save()
    context={'form':form,'caught_pokemons':CaughtPokemon.objects.all()}
    return render(request,'pages/poketype.html',context)

"""
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
"""





            
           
            
   
  








# Create your views here.
