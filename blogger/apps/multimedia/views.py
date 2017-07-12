# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *

template_dir = 'multimedia/'

class InstitucionMultimediaView(ListView):
	model = Multimedia
	paginate_by = 20
	template_name = template_dir+'lista_multimedia.html'

	def get_context_data(self, **kwargs):
		institucion = Institucion.objects.get(slug_institucion = self.kwargs['slug'])
		context = super(InstitucionMultimediaView, self).get_context_data(**kwargs)
		context['title'] = 'Multimedia'
		context['breadcrumb'] = '<li><a href="'+reverse('institucion', kwargs = {'slug': self.kwargs['slug']})+'">'+institucion.nombre_institucion+'</a></li><li><a href="'+reverse('institucion_multimedia', kwargs = {'slug': self.kwargs['slug']})+'">Multimedia</a></li>'
		context['object'] = institucion
		return context

	def get_queryset(self):
		return super(InstitucionMultimediaView, self).get_queryset().filter(institucion__slug_institucion = self.kwargs['slug']).order_by('-pk')

class InstitucionMultimediaCrearView(CreateView):
	template_name = 'layout/form_general.html'
	success_message = 'Contenido agregado correctamente'
	form_class = MultimediaForm

	def get_context_data(self, **kwargs):
		context = super(InstitucionMultimediaCrearView, self).get_context_data(**kwargs)
		context['title'] = 'Agregar Multimedia'
		context['url'] = reverse('institucion_multimedia_add', kwargs = {'slug': self.kwargs['slug']})
		return context

	def form_valid(self, form):
		form.instance.institucion = Institucion.objects.get(slug_institucion = self.kwargs['slug'])
		form.save()
		return super(InstitucionMultimediaCrearView, self).form_valid(form)

	def get_success_url(self):
		return reverse('institucion_multimedia', kwargs = {'slug': self.kwargs['slug']})