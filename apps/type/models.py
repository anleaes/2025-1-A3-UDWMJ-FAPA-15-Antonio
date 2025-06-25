from django.db import models

class Type(models.Model):
    description = models.CharField('Descrição', max_length=100)

    class Meta:
        db_table = 'CORE_TYPE'

    def __str__(self):
        return str(self.description)
