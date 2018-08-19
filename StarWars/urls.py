from StarWars import views
from django.conf.urls import url

"""
This file maps the URLs with the view functions.
"""

urlpatterns = [
    url(r'^$', views.Index, name='Index'),
    url(r'^load_data/$', views.HomePage, name='HomePage'),
    url(r'^Search_Planet/$', views.SearchPlanet, name='SearchPlanet'),
    url(r'^Display_Planet/$', views.DisplayPlanet, name='DisplayPlanet'),
    url(r'^add_data/$', views.add_data, name='add_data'),
    url(r'^add_Planets_data/$', views.add_planet_data, name='add_planet_data'),
    url(r'^Display_Saved_Data/$', views.display_saved_data, name='display_saved_data'),
]
