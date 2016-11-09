from django.conf.urls import url
from django.contrib.auth.views import login,logout
from . import views

urlpatterns = [
	url(r'^login/$', login, name="login"),
	url(r'^registros/$', views.Registros.as_view(), name="registros"),
	url(r'^registros/(?P<id>\d+)$', views.Detalle.as_view(), name="detalle")
]