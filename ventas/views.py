from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Venta
from .forms import VentaForm
from django.template.loader import render_to_string
from django.contrib.auth.models import User

class Dashboard(View):
	def get(self,request):
		template_name = "ventas/dashboard.html"
		ventas_realizadas = Venta.objects.filter(vendedor = request.user)
		context = {'ventas_realizadas':ventas_realizadas}
		return render(request, template_name, context)

class Create(View):
	def get(self,request):
		template_name = "ventas/create.html"
		form_venta = VentaForm()
		context = {
		'form_venta':form_venta
		}
		return render(request, template_name, context)
	def post(self,request):
		venta = VentaForm(request.POST)
		if venta.is_valid():
			venta_save = venta.save(commit=False)
			venta_save.vendedor = request.user
			venta.save()
			return redirect('ventas:dashboard')
		else:
			template_name = "ventas/create.html"
			context = {'form_venta':venta}
			return render(request, template_name, context)


class Finalizadas(View):
	pass

class Finalizadas_Detalle(View):
	pass
