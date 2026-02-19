from django.db import models
from django.utils.translation import gettext_lazy as _

class tablero_model(models.Model):

    class estado_tablero(models.TextChoices):
        EVALUACION = 'Evaluación', _('Evaluación')
        ESPERA = 'Espera', _('Espera')
        REPARACION = 'Reparación', _('Reparación')
        ENTREGADO = 'Entregado', _('Entregado')

    guia = models.CharField(max_length=255, verbose_name='presupuesto' ,null=True, blank=True)
    recibio = models.CharField(max_length=255, verbose_name='recibio', null=True, blank=True)
    lista = models.IntegerField(verbose_name='Numéro de lista', null=True, blank=True)
    desc = models.TextField(verbose_name='Descripción', null=True, blank=True)
    # estado = models.CharField(max_length=255, verbose_name='Estado', choices=estado_tablero.choices, default=estado_tablero.EVALUACION, null=True, blank=True)
    cliente = models.CharField(max_length=255, verbose_name='Cliente', null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True)
    # imagen = models.CharField(max_length=255, verbose_name='Imagen', null=True, blank=True)
    fecha_recepcion = models.DateTimeField(verbose_name='Fecha de recepción', null=True, blank=True)


    class Meta:
        verbose_name="Trabajo"
        verbose_name_plural='Trabajos'

    def __str__(self):
        return self.guia