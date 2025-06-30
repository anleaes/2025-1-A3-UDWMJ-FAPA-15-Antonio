from django.db import models

class Type(models.Model):
    description = models.CharField('Descrição', max_length=100)

    # Este método sobrescreve o save para garantir que o campo de descrição seja salvo em letras maiúsculas no banco de dados.
    def save(self, *args, **kwargs):
        if self.description:
            self.description = self.description.upper()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'CORE_TYPE'

    def __str__(self):
        return str(self.description)
