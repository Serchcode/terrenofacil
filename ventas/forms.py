from django import forms 
from .models import Venta

class VentaForm(forms.ModelForm):
	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '* Nombre(s)','class':'validate form-control formclass','name':'name','required':'true'}))
	apellidos = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'* Apellidos','class':'validate form-control formclass','name':'apellidos','required':'true'}))
	telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '* Teléfono','class':'validate form-control formclass','name':'tel','type':'number','maxlength':'50','required':'true'}))
	telefono_alterno = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Teléfono Alternativo','class':'form-control formclass','name':'tel','type':'number','maxlength':'50'}))
	correo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '* Correo electrónico','class':'validate form-control formclass','type':'email','required':'true'}))
	correo_alterno = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Correo alternativo','class':'form-control formclass','type':'email'}))
	tamano = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '* Tamaño del terreno vendido','class':'validate form-control formclass','type':'text','required':'true'}))
	plazo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '* Plazo para liquidar terreno','class':'validate form-control formclass','type':'text','required':'true'}))
	ubicacion = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'* Describe la ubicación','class':'validate form-control formclass','required':'true'}))
	class Meta:
		model = Venta
		fields = ['nombre','apellidos','correo','correo_alterno','telefono','telefono_alterno','tamano','plazo',
		'ubicacion']