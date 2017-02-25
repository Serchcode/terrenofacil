from django.db import models
from django.contrib.auth.models import User

class Venta(models.Model):
	vendedor = models.ForeignKey(User,related_name='vendedor')
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=140)
	telefono = models.CharField(max_length=13)
	telefono_alterno = models.CharField(max_length=16, blank=True, null=True)
	correo = models.EmailField(max_length=140)
	correo_alterno = models.EmailField(max_length=140, blank=True, null=True)
	tamano = models.CharField(max_length=50)
	plazo = models.CharField(max_length=50)
	fecha = models.DateField(auto_now_add=True, blank=True,null=True)
	hora = models.TimeField(auto_now_add=True, blank=True, null=True)
	ubicacion = models.TextField()

	def __str__(self):
		return '{} vendió terreno a {} {} el {} a las {}'.format(self.vendedor.username, self.nombre, self.apellidos,
			self.fecha, self.hora)

	class Meta:
		ordering = ('-fecha','-hora') 