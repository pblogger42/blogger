from blogger.apps.principal.decorators import user_is_entry_author
from django.conf.urls import patterns, url, include
from .views import *

multimedia_action_url = [
	url(r'^$', InstitucionMultimediaDetalleView.as_view(), name = 'institucion_multimedia_detalle'),
]

urlpatterns = patterns('blogger.apps.multimedia.views',
	url(r'^$', InstitucionMultimediaView.as_view(), name = 'institucion_multimedia'),
	url(r'^(?P<slug_2>[\w-]+)/', include(multimedia_action_url)),
	url(r'^agregar/$', user_is_entry_author(InstitucionMultimediaCrearView.as_view()), name = 'institucion_multimedia_add'),
)