from django import forms 
from .models import Cliente, Comentarios
from django.contrib.auth.models import User

class ClienteForm(forms.ModelForm):

	LENGTH_CHOICES = (
	('','Seleccione un tamaño'),
	('120','120 m'),
	('150','150 m'),
	('300','300 m'),
	('other','Otro'),
	)

	PLAZO_PAGO_CHOICES = (
		('','Seleccione un plazo'),
		('1 año','1 Año'),
		('2 años','2 Años'),
		('3 años','3 Años'),
		('5 años','5 Años'),
		)

	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre(s)','class':'validate form-control formclass','name':'name','required':'true'}))
	apellidos = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Apellidos','class':'validate form-control formclass','name':'apellidos','required':'true'}))
	telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Teléfono','class':'validate form-control formclass','name':'tel','type':'number','maxlength':'13','required':'true'}))
	correo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Correo electrónico','class':'validate form-control formclass','type':'email','required':'true'}))
	tamano = forms.CharField(widget=forms.Select(choices=LENGTH_CHOICES, attrs={'class':'selectpicker form-control formclass','required':'true'}))
	plazo = forms.CharField(widget=forms.Select(choices=PLAZO_PAGO_CHOICES, attrs={'class':'selectpicker form-control formclass','required':'true'}))



	class Meta:
		model = Cliente
		fields = ['nombre','apellidos','telefono','correo','tamano','plazo']

class EditRegistro(forms.ModelForm):
	
	cita = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Próxima cita: ','class':'validate form-control formclass datepicker','name':'cita','id':'cita','aria-describedby':'addon','readonly':'true'}))

	class Meta:
		model = Cliente
		fields = ['cita']

class CommentsForm(forms.ModelForm):


	coment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ingresa comentario','class':'validate form-control formclass','name':'comentario','id':'comentario','rows':'4'}))
	
	#telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Teléfono','class':'validate form-control formclass','name':'tel','type':'number','maxlength':'13','required':'true'}))
	#correo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Correo electrónico','class':'validate form-control formclass','type':'email','required':'true'}))

	class Meta:
		model = Comentarios
		fields = ['coment']

class EditClientUser(forms.ModelForm):

	username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate form-control formclass','name':'username','required':'true'}))
	class Meta:
		model = User
		fields = ['username']	

