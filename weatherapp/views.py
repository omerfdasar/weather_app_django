from django.shortcuts import render
from decouple import config
import requests
from pprint import pprint
from django.contrib import messages

from weatherapp.models import City


def home(request):
    API_KEY = config('API_KEY')

    u_city = request.GET.get('name')
    if u_city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={u_city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.ok:
            content = response.json()
            r_city = content['name']
            if City.objects.filter(name=r_city):
                messages.warning(request, "Entered city is already exists.")
            else:
                City.objects.create(name=r_city)
                messages.success(request, "City succesfully added to list.")
        else:
            messages.error(request, 'The city that you entered is not found!')

    city_data = []


    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    content = response.json()

    context = {
        'city':  content['name'],
        'temp':   content['main']['temp'],
        'icon':   content['weather'][0]['icon'],
        'desc':   content['weather'][0]['description'],
    }

    return render(request, "weatherapp/home.html", context)
