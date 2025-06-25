from django.db import models

# Modelo para pessoas (pacientes)
class Person(models.Model):
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    birth_date = models.DateField('Data de nascimento', blank=True, null=True)
    address = models.TextField('Endereço', blank=True, null=True)
    phone = models.CharField('Telefone', max_length=20, blank=True, null=True)
    email = models.EmailField('E-mail', blank=True, null=True)

    class Meta:
        db_table = 'CORE_PERSON'

    def __str__(self):
        return str(self.name)
