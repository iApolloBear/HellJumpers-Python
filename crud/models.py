from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Promocion(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    vigencia = models.CharField(max_length=30)
    sublineas = models.CharField(max_length=40)
    dirigido = models.CharField(max_length=40)
    restricciones = models.CharField(max_length=200)
    avances = models.CharField(max_length=100)
    descuento = models.CharField(max_length=20)
    cartera = models.CharField(max_length=20)
    image = models.ImageField(upload_to='promocion/images/')

    def __str__(self):
        return self.nombre


class Concurso(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    vigencia = models.CharField(max_length=30)
    dirigido = models.CharField(max_length=40)
    sublineas = models.CharField(max_length=40)
    restricciones = models.CharField(max_length=200)
    cartera = models.CharField(max_length=20)
    image = models.ImageField(upload_to='concurso/images/')

    def __unicode__(self,):
        return self.nombre


class Client(models.Model):
    sucursal = models.CharField(max_length=5)
    cartera = models.CharField(max_length=6)
    clientes = models.CharField(max_length=150)
    fecha_alta = models.CharField(max_length=10, default='')
    saldo = models.FloatField()

    def __str__(self):
        return self.clientes

