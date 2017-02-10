from django.conf.urls import url
from . import views

urlpatterns	= [
	url(r'^$', views.Dashboard.as_view(), name="dashboard"),
	url(r'^create/$', views.Create.as_view(), name="create"),
	url(r'^finalizadas/$', views.Finalizadas.as_view(),name="finalizadas"),
	url(r'^finalizadas/(?P<id>\d+)$', views.Finalizadas_Detalle.as_view(),name="finalizadas_detail"),
	url(r'^editar/(?P<id>\d+)$', views.Editar.as_view(), name="edit")
]	