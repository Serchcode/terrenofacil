from django.shortcuts import render
from django.views.generic import View, TemplateView
from Clientes.forms import ClienteForm
from Clientes.models import Cliente

class HomeView(View):
	def get(self,request):
		template_name="index.html"
		return render(request,template_name)

class HolaView(View):
	def get(self, request):
		template_name="hola.html"
		form = ClienteForm
		context = {'form':form,}
		return render(request,template_name,context)

	def post(self,request):
		template_name="hola.html"
		dataForm = ClienteForm(data=request.post)
		if dataForm.is_valid():
			saveForm = dataForm.save(commit=False)
			saveForm.save()
			return redirect('main:home')
		else:
			context = {'form':dataForm}
			return render(request,template_name,context)
