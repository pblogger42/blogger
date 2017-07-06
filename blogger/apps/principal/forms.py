# -*- encoding: utf-8 -*-
from mail_templated import send_mail
from django.conf import settings
from django.forms import *
from django import forms
from .models import *

class ContactForm(forms.Form):
	fullname = forms.CharField(label = 'Nombre completo', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Digite el nombre completo'}))
	cellphone = forms.CharField(label = 'Número telefónico', widget = forms.TextInput(attrs = {'class': 'form-control only-number', 'placeholder': 'Digite el número telefónico'}))
	email = forms.CharField(label = 'Email', widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'Digite el correo electrónico'}))
	mensaje = forms.CharField(label = 'Mensaje', widget = forms.Textarea())

	def send_email(self, slug_institucion, request):
		institucion = Institucion.objects.get(slug_institucion = slug_institucion)
		for users in institucion.userprofile_set.all():
			data = {
				'domain': request,
				'protocol': 'http://',
				'subject': 'Contácto',
				'args': {
					'nombre_admin': users.user.first_name+' '+users.user.last_name,
					'email': self.cleaned_data['email'],
					'nombre_completo': self.cleaned_data['fullname'],
					'numero_telefonico': self.cleaned_data['cellphone'],
					'mensaje_contact': self.cleaned_data['mensaje']
				}
			}
			send_mail('email/email_contact.tpl', data, settings.EMAIL_HOST_USER, [users.user.email])