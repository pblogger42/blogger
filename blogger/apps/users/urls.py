from django.contrib.auth.decorators import user_passes_test, permission_required
from django.conf.urls import patterns, url, include
from django.contrib.auth import views as auth_views
from .views import *

login_forbidden = user_passes_test(lambda u: u.is_anonymous(), '/')

urlpatterns = patterns('blogger.apps.users.views',
	url(r'^ingreso/$', login_forbidden(auth_views.login), {'template_name': 'usuario/form_login.html', 'extra_context': {'title': 'Ingresar'}}, name = 'login'),
	url(r'^salir/$', auth_views.logout, {'next_page': '/'}, name = 'logout'),
	url(r'^registro/$', login_forbidden(UserRegistrateView.as_view()), name = 'registrate'),
	url(r'^change-password/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', login_forbidden(PasswordResetConfirmView.as_view()),name='reset_password_confirm'),
	url(r'^forgot-password/$', login_forbidden(ResetPasswordRequestView.as_view()), name = 'reset_password'),
)