# -*- encoding: utf-8 -*-
from blogger.apps.principal.forms import SuscribeForm
from django.core.urlresolvers import reverse
from blogger.apps.principal.models import *
from blogger.apps.entradas.models import *
from django import template
import datetime

register = template.Library()

@register.assignment_tag
def build_menu_proyecto():
	data_institucion = ''
	for institucion in Institucion.objects.all():
		data_institucion += '<li><a href="'+reverse('institucion', kwargs = {'slug': institucion.slug_institucion})+'">'+institucion.nombre_institucion+'</a></li>'
	return data_institucion

@register.filter
def ultimas_entradas(slug_institucion):
	return Entrada.objects.filter(institucion__slug_institucion = slug_institucion).order_by('-numero_visitas')[:5]

@register.inclusion_tag('principal/email_suscribe.html')
def template_suscribe_form(request_path):
	return {'form': SuscribeForm(), 'request_path': request_path}