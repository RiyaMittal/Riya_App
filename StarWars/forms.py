from django import forms
from StarWars.models import Planets, Movies


class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ("title", "episode_id", "director", "producer")


class PlanetsForm(forms.ModelForm):
    class Meta:
        model = Planets
        fields = '__all__'
