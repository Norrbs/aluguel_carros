from django.db import models

# Create your models here.

class Carro(models.Model):
  marca = models.CharField(max_length=200)
  modelo = models.CharField(max_length=200)
  ano = models.PositiveSmallIntegerField(default='2023')
  cor = models.CharField(max_length=200)
  km_rodados = models.PositiveBigIntegerField(default=0)
  foto = models.ImageField(upload_to='avatares', blank=True, null=True)
  preco = models.PositiveBigIntegerField()

  manual = "ma"
  automatico = "au"
  cambio_escolhas = [
    (manual,"Manual"),
    (automatico,"Automático")
  ]
  cambio = models.CharField(
        max_length=2,
        choices=cambio_escolhas,
        default=manual,
  )

  def __str__(self):
    return self.modelo


