from django.db import models


class Cliente(models.Model):

	LENGTH_CHOICES = (
	('120','120 m'),
	('150','150 m'),
	('300','300 m'),
	('other','Otro'),
	)

	PLAZO_PAGO_CHOICES = (
		('1 año','1 Año'),
		('2 años','2 Años'),
		('3 años','3 Años'),
		('5 años','5 Años'),
		)

	nombre = models.CharField(max_length=100)
	telefono = models.CharField(max_length=13)
	correo = models.EmailField(max_length=140)
	tamano = models.CharField(max_length=5,choices=LENGTH_CHOICES,default="Escoge un tamaño")
	plazo = models.CharField(max_length=10, choices=PLAZO_PAGO_CHOICES, default="Escoge un plazo")
	fecha = models.DateField(auto_now=True, blank=True,null=True)
	hora = models.TimeField(auto_now=True, blank=True, null=True)
	comentario = models.TextField(blank=True, null=True)
	cerrado = models.BooleanField(default=False, blank=True)
	cita = models.DateField(default=None, blank=True, null=True)

	
	def __str__(self):
		return 'Cliente: {} se registró el {} a las {}'.format(self.nombre, self.fecha, self.hora)

	class Meta:
		ordering = ('-fecha','-hora')

class Administradores(models.Model):
	nombre = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=140, blank=True, null=True)
	correo = models.EmailField(max_length=140, blank=True, null=True)
	username = models.CharField(max_length=140)
# Create your models here.
