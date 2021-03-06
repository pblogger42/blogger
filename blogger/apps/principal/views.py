# -*- encoding: utf-8 -*-
from django.contrib.messages.views import SuccessMessageMixin
from blogger.apps.users.models import UserProfile
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
		context['instituciones'] = Institucion.objects.filter(estado = '1')
		context['sliders'] = Slider.objects.all()
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

class InstitucionCreateView(SuccessMessageMixin, CreateView):
	template_name = 'layout/form_general.html'
	success_message = 'Institución creado correctamente'
	form_class = InstitucionForm

	def get_context_data(self, **kwargs):
		context = super(InstitucionCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Agregar institución'
		context['url'] = reverse('institucion_crear')
		return context

	def form_valid(self, form):
		institucion = form.save(commit = True)
		profile_user = UserProfile.objects.get(user = self.request.user)
		profile_user.institucion = institucion
		profile_user.save()
		return HttpResponseRedirect(self.get_success_url(institucion))

	def get_success_url(self, institucion):
		return reverse('institucion', kwargs = {'slug': institucion.slug_institucion})

class InstitucionEditarView(SuccessMessageMixin, UpdateView):
	model = Institucion
	template_name = 'layout/form_general.html'
	success_message = 'Institución actualizada correctamente'
	form_class = InstitucionForm

	def get_context_data(self, **kwargs):
		context = super(InstitucionEditarView, self).get_context_data(**kwargs)
		context['title'] = 'Actualizar institución'
		context['url'] = reverse('institucion_editar', kwargs = {'slug': self.kwargs['slug']})
		return context

	def get_object(self):
		return Institucion.objects.get(slug_institucion = self.kwargs['slug'])

	def get_success_url(self):
		return reverse('institucion', kwargs = {'slug': self.object.slug_institucion})

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

class InstitucionUsuarioView(ListView):
	model = UserProfile
	template_name = template_dir+'lista_usuario.html'

	def get_context_data(self, **kwargs):
		institucion = Institucion.objects.get(slug_institucion = self.kwargs['slug'])
		context = super(InstitucionUsuarioView, self).get_context_data(**kwargs)
		context['title'] = 'Detalle de la entrada'
		context['object'] = institucion
		context['breadcrumb'] = '<li><a href="'+reverse('institucion', kwargs = {'slug': self.kwargs['slug']})+'">'+institucion.nombre_institucion+'</a></li><li><a href="'+reverse('institucion_usuario', kwargs = {'slug': self.kwargs['slug']})+'">Usuarios</a></li>'
		return context

	def get_queryset(self):
		return super(InstitucionUsuarioView, self).get_queryset().filter(institucion__slug_institucion = self.kwargs['slug'])

class InstitucionUsuarioAddView(FormView):
	template_name = 'layout/form_general.html'
	success_message = 'Usuario agregado'
	form_class = InstitucionUsuarioForm

	def get_context_data(self, **kwargs):
		institucion = Institucion.objects.get(slug_institucion = self.kwargs['slug'])
		context = super(InstitucionUsuarioAddView, self).get_context_data(**kwargs)
		context['url'] = reverse('institucion_usuario_add', kwargs = {'slug': self.kwargs['slug']})
		context['title'] = 'Agregar usuario'
		return context

	def form_valid(self, form):
		form.save(self.kwargs['slug'])
		return super(InstitucionUsuarioAddView, self).form_valid(form)

	def get_success_url(self):
		return reverse('institucion_usuario', kwargs = {'slug': self.kwargs['slug']})

def InstitucionUsuarioDeleteView(request, slug, pk_userprofile):
	user_institucion = UserProfile.objects.get(pk = pk_userprofile)
	user_institucion.institucion = None
	user_institucion.save()
	return HttpResponseRedirect(reverse('institucion', kwargs = {'slug': slug}))

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