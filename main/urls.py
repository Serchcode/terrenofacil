from django.conf.urls import url
from . import views

urlpatterns=[

	url(r'^$',views.HomeView.as_view(),name='home'),
	url(r'^hola/$',views.HolaView.as_view(), name='hola'),
	url(r'^gracias/$', views.GraciasView.as_view(),name="gracias")
	
]