# -*- encoding: utf-8 -*-
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy, reverse
from blogger.apps.principal.models import *
from django.shortcuts import render
from django.views.generic import *
from django.db.models import Q
from .models import *
from .forms import *

template_dir = 'entradas/'

class InstitucionEntradaView(ListView):
	model = Entrada
	paginate_by = 20
	template_name = template_dir+'lista_entrada.html'

	def get_context_data(self, **kwargs):
		context = super(InstitucionEntradaView, self).get_context_data(**kwargs)
		context['title'] = 'Entradas'
		context['object'] = Institucion.objects.get(slug_institucion = self.kwargs['slug'])
		return context

	def get_form_kwargs(self):
		kwargs = super(InstitucionEntradaView, self).get_form_kwargs()
		kwargs['q'] = self.request.GET.get('q')
		return kwargs

	def get_queryset(self):
		queryset = super(InstitucionEntradaView, self).get_queryset().filter(institucion__slug_institucion = self.kwargs['slug']).order_by('-pk')
		if self.request.GET.get('q') is not None:
			find_by = self.request.GET.get('q')
			queryset = queryset.filter(Q(titulo_entrada__icontains = find_by) | Q(descripcion_entrada__icontains = find_by))
		return queryset

class InstitucionEntradaDetalleView(ListView):
	model = Comentario
	paginate_by = 5
	template_name = template_dir+'detalle_entrada.html'

	def get_context_data(self, **kwargs):
		context = super(InstitucionEntradaDetalleView, self).get_context_data(**kwargs)
		context['title'] = 'Detalle de la entrada'
		context['object'] = Institucion.objects.get(slug_institucion = self.kwargs['slug'])
		context['entrada'] = Entrada.objects.get(slug_entrada = self.kwargs['slug_2'])
		return context

	def get_queryset(self):
		return super(InstitucionEntradaDetalleView, self).get_queryset().filter(entrada__slug_entrada = self.kwargs['slug_2']).order_by('-fecha')

class InstitucionEntradaCrearView(SuccessMessageMixin, CreateView):
	template_name = template_dir+'form_entrada.html'
	success_message = 'Entrada agregada correctamente'
	form_class = EntradaForm

	def get_context_data(self, **kwargs):
		context = super(InstitucionEntradaCrearView, self).get_context_data(**kwargs)
		context['title'] = 'Agregar entrada'
		context['object'] = Institucion.objects.get(slug_institucion = self.kwargs['slug'])
		context['url'] = reverse('institucion_entrada_crear', kwargs = {'slug': self.kwargs['slug']})
		return context

	def form_valid(self, form):
		form.instance.usuario = self.request.user
		form.instance.institucion = Institucion.objects.get(slug_institucion = self.kwargs['slug'])
		form.save()
		return super(InstitucionEntradaCrearView, self).form_valid(form)

	def get_success_url(self):
		return reverse('detalle_entrada', kwargs = {'slug': self.kwargs['slug'], 'slug_2': self.object.slug_entrada})

class InstitucionEntradaEditarView(SuccessMessageMixin, UpdateView):
	model = Entrada
	template_name = template_dir+'form_entrada.html'
	success_message = 'Entrada actualizada correctamente'
	form_class = EntradaForm

	def get_context_data(self, **kwargs):
		context = super(InstitucionEntradaEditarView, self).get_context_data(**kwargs)
		context['title'] = 'Actualizar entrada'
		context['object'] = Institucion.objects.get(slug_institucion = self.kwargs['slug'])
		context['url'] = reverse('institucion_entrada_editar', kwargs = {'slug': self.kwargs['slug'], 'slug_2': self.kwargs['slug_2']})
		return context

	def get_object(self):
		return Entrada.objects.get(slug_entrada = self.kwargs['slug_2'])

	def get_success_url(self):
		return reverse('detalle_entrada', kwargs = {'slug': self.kwargs['slug'], 'slug_2': self.object.slug_entrada})

class InstitucionComentarioCrearView(SuccessMessageMixin, CreateView):
	template_name = 'layout/form_general.html'
	success_message = 'Comentario agregado correctamente'
	form_class = ComentarioForm

	def get_context_data(self, **kwargs):
		context = super(InstitucionComentarioCrearView, self).get_context_data(**kwargs)
		context['title'] = 'Agregar comentario'
		context['object'] = Institucion.objects.get(slug_institucion = self.kwargs['slug'])
		context['url'] = reverse('institucion_comentario_crear', kwargs = {'slug': self.kwargs['slug'], 'slug_2': self.kwargs['slug_2']})
		return context

	def form_valid(self, form):
		form.instance.usuario = self.request.user
		form.instance.entrada = Entrada.objects.get(slug_entrada = self.kwargs['slug_2'])
		form.save()
		return super(InstitucionComentarioCrearView, self).form_valid(form)

	def get_success_url(self):
		return reverse('detalle_entrada', kwargs = {'slug': self.kwargs['slug'], 'slug_2': self.kwargs['slug_2']})

class InstitucionComentarioEditarView(SuccessMessageMixin, UpdateView):
	model = Comentario
	template_name = 'layout/form_general.html'
	success_message = 'Comentario actualizada}o correctamente'
	form_class = ComentarioForm

	def get_context_data(self, **kwargs):
		context = super(InstitucionComentarioEditarView, self).get_context_data(**kwargs)
		context['title'] = 'Actualizar comentario'
		context['object'] = Institucion.objects.get(slug_institucion = self.kwargs['slug'])
		context['url'] = reverse('institucion_comentario_editar', kwargs = {'slug': self.kwargs['slug'], 'slug_2': self.kwargs['slug_2'], 'pk': self.kwargs['pk']})
		return context

	def get_success_url(self):
		return reverse('detalle_entrada', kwargs = {'slug': self.kwargs['slug'], 'slug_2': self.kwargs['slug_2']})