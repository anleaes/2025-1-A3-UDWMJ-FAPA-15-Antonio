from django.db import models

# Modelo para fornecedores de vacinas
class Supplier(models.Model):
    name = models.CharField('Nome', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=18, blank=True, null=True)
    address = models.TextField('Endereço', blank=True, null=True)

    class Meta:
        db_table = 'CORE_SUPPLIER'

    def __str__(self):
        return str(self.name)
