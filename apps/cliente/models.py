from django.db import models

# Create your models here.

class Persona(models.Model):
	rut = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	nacimiento = models.DateField()
	telefono = models.CharField(max_length=10)
	email = models.EmailField()