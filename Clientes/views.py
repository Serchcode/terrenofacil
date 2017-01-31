from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .models import Cliente
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import EditRegistro, CommentsForm, ClienteForm, EditClientUser

class Registros	(View):
	@method_decorator(login_required)
	def get(self, request):
		if request.user.is_superuser:
			template_name = "clientes/registros.html"
			registros = Cliente.objects.all()
			counter = Cliente.objects.all().count()
			context = {'registros':registros, 'counter':counter}
			return render(request, template_name, context)
		else:
			return redirect('seguimiento:dashboard')

class Detalle (View):
	@method_decorator(login_required)
	def get(self, request, id):
		if request.user.is_superuser:
			template_name = "clientes/detalle.html"
			registro = Cliente.objects.get(pk = id)
			comentarios = registro.comentarios.all()
			editform = EditRegistro(instance=registro)
			comentariosform = CommentsForm()
			context = {'editform':editform,'registro':registro,'comentarios':comentarios,'comentariosform':comentariosform}
			return render(request, template_name, context)
		else:
			raise PermissionDenied

	@method_decorator(login_required)
	def post(self,request, id):
		if request.user.is_superuser:
			data = request.POST.get('hidden')
			print(data)
			aidi = request.POST.get('aidi')
			print(aidi)
			#cliente = Cliente.objects.get(pk = aidi)
			if data == 'comentarioBtn':
				form = CommentsForm(request.POST)
				form_save = form.save(commit=False)
				if form_save.coment == '':
					messages.error(request, "Comentario vacio")
				else:
					form_save.cliente = Cliente.objects.get(pk = int(aidi))
					form_save.save()
					messages.success(request, "Comentario guardado")
			elif data == 'cita':
				fecha = Cliente.objects.get(pk = int(aidi))
				#fechaform = fecha.save(commit = False)
				fecha.cita = request.POST.get('cita')
				print(fecha.cita)
				fecha.save()
				#print(fecha)
				#if fecha.is_valid():
				#	fecha_save = fecha.save(commit=False)
				#	fecha_save.save()
				#	messages.success(request, "Cita actualizada")
			return redirect('seguimiento:detalle', id = int(aidi))
		else:
			raise PermissionDenied

class Dashboard(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "clientes/detalle.html"
		email_user = request.user.email
		print(email_user)
		registro = Cliente.objects.get(correo = email_user)
		comentarios = registro.comentarios.all()
		context = {'registro':registro,'comentarios':comentarios}
		return render(request, template_name, context)

class Edit(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = "clientes/editarCliente.html"
		email_user = request.user.email
		registro = Cliente.objects.get(correo = email_user)
		form_Cliente = ClienteForm(instance = registro)
		form_User = EditClientUser(instance = request.user)
		print(form_User)
		context = {
			'form_Cliente':form_Cliente,
			'form_User': form_User
		}
		return render(request, template_name, context)
	def post(self,request):
		registro = Cliente.objects.get(correo = request.user.email)
		form_Cliente = ClienteForm(data=request.POST, instance=registro)
		username_form = EditClientUser(data=request.POST)
		if form_Cliente.is_valid():
			form_Cliente_save = form_Cliente.save(commit=False)
			user_update = User.objects.get(pk=request.user.id)
			user_update.first_name = form_Cliente_save.nombre
			user_update.email = form_Cliente_save.correo
			user_update.last_name = form_Cliente_save.apellidos
			if username_form.is_valid():
				username_update = username_form.save(commit=False)
				user_update.username = username_update.username
			form_Cliente_save.save()
			user_update.save()
			messages.success(request,'Se han actualizado tus datos')
			return redirect('seguimiento:dashboard')
		else:
			messages.error(request,'Hubo un error al guardar tus datos')
			return redirect('seguimiento:edit')





class Cerrar(View):
	@method_decorator(login_required)
	def get(self, request, id):
		if request.user.is_superuser:
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
		else:
			raise PermissionDenied

class Borrar(View):
	@method_decorator(login_required)
	def get(self, request, id):
		if request.user.is_superuser:
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
