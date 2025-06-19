from django.db import models

# Create your models here.

class Vacina(models.Model):
    nome = models.CharField('Nome da Vacina', max_length=100)
    fabricante = models.CharField('Fabricante', max_length=100)
    dose = models.IntegerField('Número da Dose')
    data_aplicacao = models.DateField('Data de Aplicação')

    class Meta:
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'
        ordering = ['nome']

    def __str__(self):
        return self.nome