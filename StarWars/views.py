# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import QueryDict
from StarWars.models import Movies, Planets
from django.shortcuts import render
import requests
from StarWars.forms import MoviesForm

"""
This file defines all the functions which render the data to templates
"""

def Index(request):
    return render(request, 'StarWars/index.html')


def HomePage(request):
    url = request.GET['q']
    response = requests.get(url)
    film_data = response.json()
    planets_data = film_data['planets']
    planet_list = []

    for i in planets_data:
        resp = requests.get(i)
        planet_data_json = resp.json()
        planet_all_data = {'name': planet_data_json['name'],
                           'rotation_period': planet_data_json['rotation_period'],
                           'orbital_period': planet_data_json['orbital_period'],
                           'diameter': planet_data_json['diameter']}
        planet_list.append(planet_all_data)

    return render(request, 'StarWars/home.html', {'title': film_data['title'], "episode_id": film_data['episode_id'],
                                                  "director": film_data['director'], "producer": film_data['producer'],
                                                  'planet_list': planet_list, 'dataurl': url})


def SearchPlanet(request):
    response = requests.get('https://swapi.co/api/films/')
    film_content = response.json()
    film_results = film_content['results']
    title_list = []
    for film in film_results:
        title = film['title']
        title_list.append(title)
    return render(request, 'StarWars/SearchPlanet.html', {'titles': title_list})


def DisplayPlanet(request):
    response = requests.get('https://swapi.co/api/films/')
    film_content = response.json()
    film_results = film_content['results']
    title_list = []
    for film in film_results:
        title = film['title']
        if (title == request.GET['Titles']):
            title_list.append(film)
            break

    film_data = title_list[0]
    planets_data = film_data['planets']
    planet_list = []

    for i in planets_data:
        resp = requests.get(i)
        planet_data_json = resp.json()
        planet_all_data = {'name': planet_data_json['name'],
                           'rotation_period': planet_data_json['rotation_period'],
                           'orbital_period': planet_data_json['orbital_period'],
                           'diameter': planet_data_json['diameter']}
        planet_list.append(planet_all_data)

    return render(request, 'StarWars/DisplayPlanet.html', {'planets': planet_list})


def add_data(request):
    form = MoviesForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        movie_data_set = Movies.objects.all()
        planet_added_data = Planets.objects.all()
        return render(request, 'StarWars/Display_added_data.html',
                      {'planet_added_data': planet_added_data, 'movies_added_data': movie_data_set})

    else:
        form.errors()


def add_planet_data(request):
    data = request.body
    d = QueryDict(data)

    planet_name_list = d.getlist('name')
    planet_rotation_list = d.getlist('rotation_period')
    planet_orbital_list = d.getlist('orbital_period')

    for i in range(0, len(planet_name_list)):
        planet_name = planet_name_list[i].encode("ascii")
        planet_rotation = planet_rotation_list[i].encode("ascii")
        planet_orbital = planet_orbital_list[i].encode("ascii")
        planet_save(planet_name, planet_rotation, planet_orbital)

    movie_data_set = Movies.objects.all()
    planet_added_data = Planets.objects.all()
    return render(request, 'StarWars/Display_added_data.html',
                  {'planet_added_data': planet_added_data, 'movies_added_data': movie_data_set})


def planet_save(planet_name, planet_rotation, planet_orbital):
    planet = Planets()
    planet.name = planet_name
    planet.orbital_period = planet_orbital
    planet.rotation_period = planet_rotation
    planet.save()

def display_saved_data(request):
    movie_data_set = Movies.objects.all()
    planet_added_data = Planets.objects.all()
    return render(request, 'StarWars/Display_added_data.html',
                  {'planet_added_data': planet_added_data, 'movies_added_data': movie_data_set})
