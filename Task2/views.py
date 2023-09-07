from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TypeSearchForm
import json
import requests

def pokeshow(request):
    form=TypeSearchForm()
    pokemons=[]

    if request.method == 'POST':
        form=TypeSearchForm(request.POST)
        if form.is_valid():
            type_name=form.cleaned_data['type_name']
            url = f'https://pokeapi.co/api/v2/type/{type_name.lower()}/'
            response=requests.get(url)
            data=response.json()
            pokemons=[entry['pokemon']['name'] for entry in data['pokemon']]
            
   
    context={'form':form,'pokemons':pokemons}
    return render(request,'pages/pokeshow.html',context)
           
# Create your views here.
