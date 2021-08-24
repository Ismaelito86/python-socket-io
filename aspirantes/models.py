from django.db import models

# Create your models here.
class Aspirante(models.Model):
    """ Modelo DB para los Aspirantes """

    nombre = models.CharField(max_length=250)
    sexo = models.CharField(max_length=1, default='M')
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Aspirante'
        verbose_name_plural = 'Aspirantes'

class Habilidad(models.Model):

    nombre = models.CharField(max_length=150)
    test = models.PositiveSmallIntegerField()
    nivel = models.PositiveSmallIntegerField()
    a_experiencia = models.PositiveSmallIntegerField()
    aspirante = models.ManyToManyField(Aspirante)#on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'