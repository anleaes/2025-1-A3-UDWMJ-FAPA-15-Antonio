from django.db import models

# Modelo para vias de administração de vacina
class AdministrationRoute(models.Model):
    name = models.CharField('Via de administração', max_length=50)

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.upper()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'CORE_ADMINISTRATIONROUTE'

    def __str__(self):
        return self.name
