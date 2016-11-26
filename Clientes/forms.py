from django import forms 
from .models import Cliente

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

	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre Completo','class':'validate form-control formclass','name':'name','required':'true'}))
	telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Teléfono','class':'validate form-control formclass','name':'tel','type':'number','maxlength':'13','required':'true'}))
	correo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Correo electrónico','class':'validate form-control formclass','type':'email','required':'true'}))
	tamano = forms.CharField(widget=forms.Select(choices=LENGTH_CHOICES, attrs={'class':'selectpicker form-control formclass','required':'true'}))
	plazo = forms.CharField(widget=forms.Select(choices=PLAZO_PAGO_CHOICES, attrs={'class':'selectpicker form-control formclass','required':'true'}))



	class Meta:
		model = Cliente
		fields = ['nombre','telefono','correo','tamano','plazo']

class EditRegistro(forms.ModelForm):


	comentario = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ingresa comentario','class':'validate form-control formclass','name':'comentario','id':'comentario','rows':'4'}))
	cita = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Próxima cita: ','class':'validate form-control formclass datepicker','name':'cita','id':'cita','aria-describedby':'addon','readonly':'true'}))
	#telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Teléfono','class':'validate form-control formclass','name':'tel','type':'number','maxlength':'13','required':'true'}))
	#correo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Correo electrónico','class':'validate form-control formclass','type':'email','required':'true'}))
	



	class Meta:
		model = Cliente
		fields = ['comentario','cita']
