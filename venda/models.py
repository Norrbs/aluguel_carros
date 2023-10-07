from django.db import models

# Create your models here.

class Carro(models.Model):
  modelo = models.CharField(max_length=200)
