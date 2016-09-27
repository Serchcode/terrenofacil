from django import forms 
from .models import Cliente

class ClienteForm(forms.ModelForm):

	LENGTH_CHOICES = (
	('','Seleccione un tamaño'),
	('120','120m'),
	('150','150m'),
	('300','300m'),
	('other','Otro'),
	)

	PLAZO_PAGO_CHOICES = (
		('','Seleccione un plazo'),
		('1 año','1 Año'),
		('2 años','2 Años'),
		('3 años','3 Años'),
		('5 años','5 Años'),
		)

	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre Completo','class':'validate form-control','name':'name'}))
	telefono = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Teléfono','class':'validate form-control','name':'tel'}))
	correo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Correo electrónico','class':'validate form-control'}))
	tamano = forms.CharField(widget=forms.Select(choices=LENGTH_CHOICES, attrs={'class':'selectpicker form-control'}))
	plazo = forms.CharField(widget=forms.Select(choices=PLAZO_PAGO_CHOICES, attrs={'class':'selectpicker form-control'}))



	class Meta:
		model = Cliente
		fields = ['nombre','telefono','correo','tamano','plazo']