# -*- encoding: utf-8 -*-
from django.forms import *
from django import forms
from .models import *

class MultimediaForm(forms.ModelForm):
	class Meta:
		model = Multimedia
		fields = '__all__'
		exclude = ('institucion', 'slug_multimedia')
		widgets = {
			'nombre_multimedia': TextInput(attrs = {'class': 'form-control', 'maxlength': '45', 'required': True}),
			'video_multimedia': TextInput(attrs = {'class': 'form-control', 'maxlength': '255'})
		}
		labels = {
			'nombre_multimedia': 'Nombre',
			'tipo_multimedia': 'Tipo',
			'image_multimedia': 'Imagen',
			'video_multimedia': 'URL video'
		}

	def __init__(self, *args, **kwargs):
		super(MultimediaForm, self).__init__(*args, **kwargs)
		self.fields['tipo_multimedia'].widget.attrs.update({'required': True, 'class': 'form-control'})