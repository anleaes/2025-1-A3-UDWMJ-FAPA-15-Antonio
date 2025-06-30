from django.db import models

# Modelo para fornecedores de vacinas
class Supplier(models.Model):
    name = models.CharField('Nome', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=18, blank=True, null=True)
    address = models.TextField('Endereço', blank=True, null=True)

    # Este método sobrescreve o save para garantir que os campos de texto descritivos (ex: nome, endereço) sejam salvos em letras maiúsculas no banco de dados.
    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.upper()
        if self.address:
            self.address = self.address.upper()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'CORE_SUPPLIER'

    def __str__(self):
        return str(self.name)
