# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *

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
		institucion = Institucion.objects.get(slug_institucion = self.kwargs['slug'])
		context = super(InstitucionView, self).get_context_data(**kwargs)
		context['title'] = 'Institucion'
		context['breadcrumb'] = '<li><a href="'+reverse('institucion', kwargs = {'slug': self.kwargs['slug']})+'">'+institucion.nombre_institucion+'</a></li>'
		return context

	def get_object(self):
		return Institucion.objects.get(slug_institucion = self.kwargs['slug'])

class InstitucionContactoView(FormView):
	template_name = template_dir+'form_contacto.html'
	success_message = 'Contácto realizado'
	form_class = ContactForm

	def get_context_data(self, **kwargs):
		institucion = Institucion.objects.get(slug_institucion = self.kwargs['slug'])
		context = super(InstitucionContactoView, self).get_context_data(**kwargs)
		context['title'] = 'Contácto'
		context['object'] = institucion
		context['breadcrumb'] = '<li><a href="'+reverse('institucion', kwargs = {'slug': self.kwargs['slug']})+'">'+institucion.nombre_institucion+'</a></li><li><a href="'+reverse('institucion_contacto', kwargs = {'slug': self.kwargs['slug']})+'">'+u'Contácto'+'</a></li>'
		return context

	def form_valid(self, form):
		form.send_email(self.kwargs['slug'], self.request.META['HTTP_HOST'])
		return super(InstitucionContactoView, self).form_valid(form)

	def get_success_url(self):
		return reverse('institucion_entrada', kwargs = {'slug': self.kwargs['slug']})

class SuscribeView(FormView):
	template_name = template_dir+'email_suscribe.html'
	success_message = 'Te has suscrito'
	form_class = SuscribeForm

	def form_valid(self, form):
		form.suscribe(self.request.META['HTTP_HOST'])
		return super(SuscribeView, self).form_valid(form)

	def get_success_url(self):
		return self.request.GET.get('next')

def unsuscribe_email(request):
	SuscripcionEntrada.objects.filter(email = request.GET.get('email')).delete()
	return render(request, template_dir+'message_unsuscribe.html', {'title': 'Unsuscribe'})