from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from main import urls as mainUrls
from ventas import urls as ventasUrls
from Clientes import urls as SeguimientoUrls
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls), 
    url(r'^',include(mainUrls, namespace="main")),
    url(r'^seguimiento/', include(SeguimientoUrls, namespace="seguimiento")),
    url(r'^ventas/',include(ventasUrls, namespace="ventas")),

    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}),

]
