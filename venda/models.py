from django.db import models

# Create your models here.

class Carro(models.Model):
  TIPOS = [
        ("Manual", "Manual"),
        ("Automático", "Automático"),
  ]
    
  marca = models.CharField(max_length=200)
  modelo = models.CharField(max_length=200)
  ano = models.PositiveSmallIntegerField(default='2023')
  cor = models.CharField(max_length=200)
  km_rodados = models.PositiveBigIntegerField(default=0)
  foto = models.ImageField(upload_to='avatares', blank=True, null=True)
  preco = models.PositiveBigIntegerField()
  cambio = models.CharField("Câmbio", max_length=100, choices=TIPOS, default="Manual")

  def __str__(self):
    return self.modelo


