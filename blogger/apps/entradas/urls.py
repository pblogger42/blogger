from django.conf.urls import patterns, url, include
from .views import *

comentario_action_url = [
	url(r'^editar/$', InstitucionComentarioEditarView.as_view(), name = 'institucion_comentario_editar'),
	url(r'^eliminar/$', InstitucionComentarioEliminarView.as_view(), name = 'institucion_comentario_eliminar')
]

comentario_url = [
	url(r'^crear/$', InstitucionComentarioCrearView.as_view(), name = 'institucion_comentario_crear'),
	url(r'^(?P<pk>\d+)/', include(comentario_action_url))
]

entrada_url = [
	url(r'^$', InstitucionEntradaDetalleView.as_view(), name = 'detalle_entrada'),
	url(r'^editar-entrada/$', InstitucionEntradaEditarView.as_view(), name = 'institucion_entrada_editar'),
	url(r'^eliminar-entrada/$', InstitucionEntradaEliminarView.as_view(), name = 'institucion_entrada_eliminar'),
	url(r'^comentario/', include(comentario_url)),
]

urlpatterns = patterns('blogger.apps.entradas.views',
	url(r'^$', InstitucionEntradaView.as_view(), name = 'institucion_entrada'),
	url(r'^crear-entrada/$', InstitucionEntradaCrearView.as_view(), name = 'institucion_entrada_crear'),
	url(r'^(?P<slug_2>[\w-]+)/', include(entrada_url)),
)