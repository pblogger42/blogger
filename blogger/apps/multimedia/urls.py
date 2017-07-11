from django.conf.urls import patterns, url, include
from .views import *

urlpatterns = patterns('blogger.apps.multimedia.views',
	url(r'^$', InstitucionMultimediaView.as_view(), name = 'institucion_multimedia'),
	url(r'^agregar/$', InstitucionMultimediaCrearView.as_view(), name = 'institucion_multimedia_add'),
)