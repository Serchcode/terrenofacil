from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Cliente
from django.core.exceptions import ObjectDoesNotExist
from .forms import EditRegistro, CommentsForm

class Registros	(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "clientes/registros.html"
		registros = Cliente.objects.all()
		counter = Cliente.objects.all().count()
		context = {'registros':registros, 'counter':counter}
		return render(request, template_name, context)

	def post(self,request):
		data = request.POST.get('hidden')
		print(data)
		aidi = request.POST.get('aidi')
		print(aidi)
		#cliente = Cliente.objects.get(pk = aidi)
		if data == 'comentario':
			form = CommentsForm(request.POST)
			form_save = form.save(commit=False)
			if form_save.coment == '':
				messages.error(request, "Comentario vacio")
			else:
				form_save.cliente = Cliente.objects.get(pk = int(aidi))
				print(form_save)
				form_save.save()
				messages.success(request, "Comentario guardado")
		elif data == 'cita':
			messages.success(request, "Cita actualizada")
		return redirect('seguimiento:detalle', id = int(aidi))


class Detalle(View):
	@method_decorator(login_required)
	def get(self, request, id):
		template_name = "clientes/detalle.html"
		registro = Cliente.objects.get(pk = id)
		comentarios = registro.comentarios.all()
		editform = EditRegistro(instance=registro)
		comentariosform = CommentsForm()
		context = {'editform':editform,'registro':registro,'comentarios':comentarios,'comentariosform':comentariosform}
		return render(request, template_name, context)

	def post(self,request):
		data = request.POST.get('hidden')
		print(data)
		aidi = request.POST.get('aidi')
		print(aidi)
		return redirect('seguimiento:detalle', id = int(aidi))


class Cerrar(View):
	def get(self, request, id):
		registro = Cliente.objects.get(pk = id)
		registro.cerrado = True
		registro.save()
		check = Cliente.objects.get(pk = id)
		if check.cerrado == True:
			messages.success(request, "Se ha cerrado registro de " +registro.nombre + " exitosamente")
			return redirect('seguimiento:registros')
		else:
			messages.error(request, "No se pudo cerrar registro")
			return redirect('seguimiento:registros')

class Borrar(View):
	def get(self, request, id):
		registro = Cliente.objects.get(pk = id)
		nombre = registro.nombre
		aidi = registro.id
		registro.delete()
		#cont = Cliente.objects.get(pk = aidi).count()
		try:
			 Cliente.objects.get(pk = aidi)
		except ObjectDoesNotExist:
			messages.success(request, "Se ha eliminado a " +nombre + " exitosamente")
			return redirect('seguimiento:registros')
			#messages.error(request, "Error al eliminar a ", nombre)
			#return redirect('seguimiento:registros')

		#else:
		#	messages.success(request, "Se ha eliminado a ",nombre," exitosamente")
		#	return redirect('seguimiento:registros')
		#messages.success(request, "Hola")
		#return redirect('seguimiento:registros')
		#print("Si llego")
