from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from Clientes.forms import ClienteForm
from Clientes.models import Cliente
from django.core.mail import send_mail
from django.http import HttpResponse
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
			#asunto = 'Eso es una prueba de envio de correos'
			#mensaje = dataForm.cleaned_data['mensaje']
			#mail = EmailMessage(asunto, mensaje, to=['he195621@gmail.com'])
			saveForm = dataForm.save(commit=False)
			#send_mail(
			#	"Invitacion a los XV de ruby",
			#	"Va aver muchas cosas wuuu",
			#	"he195621@uaeh.edu.mx",
			#	["luis.arma92@gmail.com"], fail_silently=False
			#)
			saveForm.save()
			#DAtos del cliente papud
			#print('Sa guardan muchos datos wuuuuu')
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
			#mail.send()
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
	subject = data['asunto']
	to = [data['correo_cliente']]
	from_email = 'he195621@gmail.com'
	messages = get_template('correo.html').render(Context(ctx))
	msg = EmailMessage(subject,message,to=to,from_email=from_email)
	msg.send()
