from django.shortcuts import render
from django.views.generic import *
from .models import *

template_dir = 'principal/'

class InicioTemplateView(TemplateView):
	template_name = template_dir+'home.html'

	def get_context_data(self, **kwargs):
		context = super(InicioTemplateView, self).get_context_data(**kwargs)
		context['instituciones'] = Institucion.objects.all()
		context['title'] = 'Bienvenido'
		return context

class InstitucionView(DetailView):
	model = Institucion
	template_name = template_dir+'detalle_institucion.html'

	def get_context_data(self, **kwargs):
		context = super(InstitucionView, self).get_context_data(**kwargs)
		context['title'] = 'Institucion'
		return context

	def get_object(self):
		return Institucion.objects.get(slug_institucion = self.kwargs['slug'])
