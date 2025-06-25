from django.db import models

# Modelo para clínicas
class Clinic(models.Model):
    name = models.CharField('Nome', max_length=100)
    address = models.TextField('Endereço', blank=True, null=True)
    phone = models.CharField('Telefone', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'CORE_CLINIC'

    def __str__(self):
        return str(self.name)
