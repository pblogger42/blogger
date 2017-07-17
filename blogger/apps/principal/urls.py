from django.conf.urls import patterns, url, include
from .views import *

pagina_institucion = [
	url(r'^acerca-de/$', InstitucionView.as_view(), name = 'institucion'),
	url(r'^contacto/$', InstitucionContactoView.as_view(), name = 'institucion_contacto'),
	url(r'^multimedia/', include('blogger.apps.multimedia.urls')),
	url(r'^', include('blogger.apps.entradas.urls')),
]

urlpatterns = patterns('blogger.apps.principal.views',
	url(r'^$', InicioTemplateView.as_view(), name = 'inicio'),
	url(r'^unsuscribe/$', 'unsuscribe_email', name = 'unsuscribe_email'),
	url(r'^suscribe/$', SuscribeView.as_view(), name = 'suscribe_email'),
	url(r'^(?P<slug>[\w-]+)/', include(pagina_institucion)),
)