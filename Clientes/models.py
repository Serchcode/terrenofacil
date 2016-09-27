from django.db import models


class Cliente(models.Model):

	LENGTH_CHOICES = (
	('120','120m'),
	('150','150m'),
	('300','300m'),
	('other','Otro'),
	)

	PLAZO_PAGO_CHOICES = (
		('1 año','1 Año'),
		('2 años','2 Años'),
		('3 años','3 Años'),
		('5 años','5 Años'),
		)

	nombre = models.CharField(max_length=100)
	telefono = models.IntegerField()
	correo = models.EmailField(max_length=140)
	tamano = models.CharField(max_length=5,choices=LENGTH_CHOICES,default="Escoge un tamaño")
	plazo = models.CharField(max_length=10, choices=PLAZO_PAGO_CHOICES, default="Escoge un plazo")
	
# Create your models here.
