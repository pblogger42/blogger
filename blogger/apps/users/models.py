from __future__ import unicode_literals

# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from blogger.apps.principal.models import *
from django.db import models

class Rol(models.Model):
	nombre_rol = models.CharField(max_length = 20)

	def __str__(self):
		return self.nombre_rol

	def __unicode__(self):
		return self.nombre_rol

class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key = True)
	rol = models.ForeignKey(Rol)
	institucion = models.ForeignKey(Institucion, null = True, blank = True)

	def __str__(self):
		return self.user.username