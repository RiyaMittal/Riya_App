# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

"""
This file define the models for StarWars App
"""

class Movies(models.Model):
    title = models.CharField(max_length=128, unique=True)
    episode_id = models.IntegerField(default=0)
    director = models.CharField(max_length=128)
    producer = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title


class Planets(models.Model):
    name = models.CharField(max_length=128)
    rotation_period = models.IntegerField(null=True)
    orbital_period = models.IntegerField(null=True)

    def __unicode__(self):
        return unicode(self.name)
