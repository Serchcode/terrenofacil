from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from Clientes.forms import ClienteForm
from Clientes.models import Cliente
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth.models import User
import string, random
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
			user = User()
			user.username = saveForm.nombre.replace(" ","")
			user.first_name = saveForm.nombre.rsplit(' ',1)[0]
			last_name = saveForm.nombre.rsplit(' ',2)[1]
			if(len(saveForm.nombre.split(' ')) > 2):
				last_name = last_name + ' ' + saveForm.nombre.rsplit(' ',2)[2]
			user.last_name = last_name
			user.email = saveForm.correo
			password = generatePassword()
			user.set_password(password)
			user.save()
			cliente_emial=dataForm.data['correo']
			cliente_nombre=dataForm.data['nombre']
			cliente_tel=dataForm.data['telefono']
			cliente_tam = dataForm.data['tamano']
			cliente_plazo = dataForm.data['plazo']
			cliente_usuario = user.username
			cliente_password = password
			mensaje='Nueva cotizacion'
			mensaje +='\nNombre:'+str(cliente_nombre)
			mensaje +='\nTelefono: '+str(cliente_tel)
			mensaje +='\nTamaño '+str(cliente_tam)
			mensaje +='\nPlazo '+str(cliente_plazo)
			mensaje +='\nUsuario '+str(cliente_usuario)
			#Enivar el correo de notificacion al Administrador
			try:
				send_mail(
					"Terreno Facil",
					mensaje,
					"provision.sistemas@gmail.com",
					["provision.sistemas@gmail.com"], fail_silently=False
				)
			#	Agradecer al cliente usando la funcion y mandano toda la data
				enviar_correo_cliente({
					'cliente_emial':cliente_emial,
					'cliente_nombre':cliente_nombre,
					'cliente_tel':cliente_tel,
					'cliente_tam':cliente_tam,
					'cliente_plazo':cliente_plazo,
					'cliente_usuario':cliente_usuario,
					'cliente_password':cliente_password
				})
			except Exception as err:
				print(err)
			return redirect('main:gracias')
		else:
			context = {'form':dataForm}
			return render(request,template_name,context)


#Ase lo mismo que home pero no se usa :(
class HolaView(View):
	def get(self, request):
		template_name="hola.html"
		form = ClienteForm
		res = send_mail(
			"Invitacion a los XV de ruby",
			"Va aver muchas cosas wuuu",
			"he195621@uaeh.edu.mx",
			["luis.arma92@gmail.com"], fail_silently=True
		)
		return HttpResponse('%s'%res)
		context = {'form':form,}
		return render(request,template_name,context)

	def post(self, request):
		template_name="hola.html"
		dataForm = ClienteForm(data=request.POST)
		if dataForm.is_valid():
			saveForm = dataForm.save(commit=False)
			send_mail(
				"Invitacion a los XV de ruby",
				"Va aver muchas cosas wuuu",
				"he195621@uaeh.edu.mx",
				["luis.arma92@gmail.com"], fail_silently=True
			)
			saveForm.save()
			#DAtos del cliente papud
			cliente_emial=dataForm.data['correo']
			cliente_nombre=dataForm.data['nombre']
			cliente_tel=dataForm.data['telefono']
			cliente_tam = dataForm.data['tamano']
			cliente_plazo = dataForm.data['plazo']
			mensaje='Nueva cotizacion yeah'
			mensaje +='Nombre:'+str(cliente_nombre)
			mensaje +='\nTelefono: '+str(cliente_tel)
			mensaje +='\nTamaño '+str(cliente_tam)
			mensaje +='\nPlazo '+str(cliente_plazo)
			#Enivar el correo de notificacion al Administrador
			try:
				send_mail(
					"Terreno Facil",
					mensaje,
					"from@example.com",
					["he195621@uaeh.edu.mx"], fail_silently=False
				)
				#Agradecer al cliente
				send_mail(
					"Gracias",
					"Estamoas atendiendo tu mensaje guapo",
					"he195621@uaeh.edu.mx",
					[cliente_emial], fail_silently=False
				)
			except:
				pass
			return redirect('main:gracias')
		else:
			context = {'form':dataForm}
			return render(request,template_name,context)

class GraciasView(View):
	def get(self, request):
		template_name="gracias.html"
		return render(request, template_name)

def enviar_correo_cliente(data):
	subject = 'Gracias'
	to = [data['cliente_emial']]
	from_email = 'provision.sistemas@gmail.com'
	data_for_render = data
	messages = get_template('email.html').render(Context(data_for_render))
	msg = EmailMessage(
		subject,
		messages,
		from_email=from_email,
		to=to,
	)
	msg.content_subtype = 'html'
	msg.send()

def generatePassword():
		password = ''
		for i in range(12):
			var = random.randint(0,51)
			password = password + string.printable[var]
		return password