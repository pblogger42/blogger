# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from blogger.apps.principal.models import *
from django import template
import datetime

register = template.Library()

@register.assignment_tag
def build_menu_proyecto():
	data_institucion = ''
	for institucion in Institucion.objects.all():
		data_institucion += '<li><a href="'+reverse('institucion', kwargs = {'slug': institucion.slug_institucion})+'">'+institucion.nombre_institucion+'</a></li>'
	return data_institucion
