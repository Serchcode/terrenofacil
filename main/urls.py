from django.conf.urls import url
from . import views

urlpatterns=[

	url(r'^$',views.HomeView.as_view(),name='_home'),
	url(r'^hola$',views.HolaView.as_view(), name='hola'),
	
]