from django.db import models


class Evolution(models.Model):
    patient = models.ForeignKey(
        'Patient',
        on_delete=models.SET_NULL,
        verbose_name='Paciente',
        null=True
    )
    prescriber = models.ForeignKey(
        'Prescriber',
        on_delete=models.SET_NULL,
        verbose_name='Fisioterapeuta',
        null=True
    )
    header = models.CharField(
        verbose_name='Cabeçalho',
        max_length=100
    )
    description = models.TextField(
        verbose_name='Descrição'
    )
    date = models.DateField(
        verbose_name='Data',
        blank=True,
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Evolução'
        verbose_name_plural = 'Evoluções'

    def __str__(self):
        return self.header

    def model_callable(self):
        return self.patient, self.prescriber


class Conduct(models.Model):
    evolution = models.ForeignKey(
        'Evolution',
        on_delete=models.SET_NULL,
        verbose_name='Evolução',
        null=True
    )
    header = models.CharField(
        verbose_name='Cabeçalho',
        max_length=100
    )
    description = models.TextField(
        verbose_name='Descrição'
    )
    date = models.DateField(
        verbose_name='Data',
        blank=True,
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Conduta'
        verbose_name_plural = 'Condutas'

    def __str__(self):
        return self.header

    def model_callable(self):
        return self.evolution
