from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from .models import Cliente

class Registros	(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "clientes/registros.html"
		registros = Cliente.objects.all()
		counter = Cliente.objects.all().count()
		context = {'registros':registros, 'counter':counter}
		return render(request, template_name, context)

class Detalle(View):
	@method_decorator(login_required)
	def get(self, request, id):
		template_name = "clientes/detalle.html"
		registro = Cliente.objects.get(pk = id)
		context = {'registro':registro}
		return render(request, template_name, context)

class Cerrar(View):
	def get(self, request, id):
		registro = Cliente.objects.get(pk = id)
		registro.cerrado = True
		registro.save()
		return redirect('seguimiento:registros')

