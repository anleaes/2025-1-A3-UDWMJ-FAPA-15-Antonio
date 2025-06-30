from django.db import models
from apps.type.models import Type
from apps.supplier.models import Supplier

# Modelo para vacinas
class Vaccine(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.CharField('Descrição', max_length=255, blank=True, null=True)
    type = models.ForeignKey(Type, verbose_name='Tipo', on_delete=models.PROTECT)  # Tipo da vacina
    doses = models.PositiveIntegerField('Número de doses', default=1)  # Total de doses
    supplier = models.ForeignKey(
        Supplier,
        verbose_name='Fornecedor',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    # Este método sobrescreve o save para garantir que o campo de nome seja salvo em letras maiúsculas no banco de dados.
    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.upper()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'CORE_VACCINE'

    def __str__(self):
        return str(self.name)
