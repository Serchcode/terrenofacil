from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from Clientes.forms import ClienteForm
from Clientes.models import Cliente

class HomeView(View):
	def get(self, request):
		template_name="hola.html"
		form = ClienteForm
		context = {'form':form,}
		return render(request,template_name,context)

	def post(self, request):
		template_name="hola.html"
		dataForm = ClienteForm(data=request.POST)
		if dataForm.is_valid():
			saveForm = dataForm.save(commit=False)
			saveForm.save()
			return redirect('main:gracias')
		else:
			context = {'form':dataForm}
			return render(request,template_name,context)

class HolaView(View):
	def get(self, request):
		template_name="hola.html"
		form = ClienteForm
		context = {'form':form,}
		return render(request,template_name,context)

	def post(self, request):
		template_name="hola.html"
		dataForm = ClienteForm(data=request.POST)
		if dataForm.is_valid():
			saveForm = dataForm.save(commit=False)
			saveForm.save()
			return redirect('main:gracias')
		else:
			context = {'form':dataForm}
			return render(request,template_name,context)

class GraciasView(View):
	def get(self, request):
		template_name="gracias.html"
		return render(request, template_name)
