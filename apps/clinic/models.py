from django.db import models

# Modelo para clínicas
class Clinic(models.Model):
    name = models.CharField('Nome', max_length=100)
    address = models.TextField('Endereço', blank=True, null=True)
    phone = models.CharField('Telefone', max_length=20, blank=True, null=True)

    # Este método sobrescreve o save para garantir que os campos de texto descritivos (ex: nome, endereço) sejam salvos em letras maiúsculas no banco de dados.
    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.upper()
        if self.address:
            self.address = self.address.upper()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'CORE_CLINIC'

    def __str__(self):
        return str(self.name)
