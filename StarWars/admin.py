# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from StarWars.models import Movies,Planets

# Register your models here.

admin.site.register(Movies)
admin.site.register(Planets)