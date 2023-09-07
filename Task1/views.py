from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
import requests


def index(request):
    response=requests.get("https://pokeapi.co/api/v2/type/")
    data=response.json()
    types=[]
    for i in data["results"]:
        types.append(i["name"])

    context={"types":types}
    return render(request, 'pages/index.html',context)
           
# Create your views here.
