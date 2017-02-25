from django.conf.urls import url
from django.contrib.auth.views import login,logout,logout_then_login
from . import views

urlpatterns = [
	url(r'^registros/$', views.Registros.as_view(), name="registros"),
	url(r'^registros/(?P<id>\d+)$', views.Detalle.as_view(), name="detalle"),
	url(r'^cerrar/(?P<id>\d+)$', views.Cerrar.as_view(), name="cerrar"),
	url(r'^$',views.VerifyUser.as_view(), name="verify_users"),
	url(r'^eliminar/(?P<id>\d+)$', views.Borrar.as_view(), name="eliminar"),
	#url(r'^dashboard/$', views.Dashboard.as_view(), name="dashboard"),
	#url(r'^dashboard/edit/(?P<id>\d+)$',views.Edit.as_view(), name="edit"),
	url(r'^login/$', login, name="login"),
	url(r'^logout/$', logout, name="logout"),
	url(r'^logout-then-login/$', logout_then_login, name="logout_then_login"),
]