from django.db import models
from apps.clinic.models import Clinic

# Modelo para registrar profissionais de saúde
class Professional(models.Model):
    name = models.CharField('Nome', max_length=100)  # Nome do profissional
    role = models.CharField('Função', max_length=50)  # Função (ex: médico, enfermeiro)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)  # Clínica onde trabalha
    cpf = models.CharField('CPF', max_length=14, unique=True)  # CPF do profissional

    # Este método sobrescreve o save para garantir que os campos de texto descritivos (ex: nome, função) sejam salvos em letras maiúsculas no banco de dados.
    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.upper()
        if self.role:
            self.role = self.role.upper()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'CORE_PROFESSIONAL'

    def __str__(self):
        return self.name  # Exibe o nome no admin e outros lugares
