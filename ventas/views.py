from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Venta
from .forms import VentaForm
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
	def get(self,request):
		template_name = "ventas/list.html"
		ventas_all = Venta.objects.all()
		paginator = Paginator(ventas_all, 10)
		page = request.GET.get('page')
		try:
			ventas = paginator.page(page)
		except PageNotAnInteger:
			ventas = paginator.page(1)
		except EmptyPage:
			ventas = paginator.page(paginator.num_pages)
		context = {'ventas':ventas,'range':paginator.page_range}
		return render(request, template_name, context)


class Finalizadas_Detalle(View):
	def get(self,request,id):
		template_name="ventas/detail.html"
		venta = Venta.objects.get(id = id)
		context = {'venta':venta}
		return render(request, template_name, context)

class Editar(View):
	pass