from django.shortcuts import render
import requests
from django.conf.urls import url
import json

def home(request):
    name = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('https://api.covidindiatracker.com/state_data.json')
    my_data =response.json()


    return render(request, 'home.html', {'my_data':my_data})

def blog(request):
    return render(request, 'blog.html')
