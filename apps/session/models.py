from django.db import models
from apps.clinic.models import Clinic #importa o modelo CLINICA
from apps.person.models import Person #Importa o modelo PESSOA 
from apps.vaccine.models import Vaccine #Importa o modelo VACINA
from apps.professional.models import Professional  #Importa o modelo PROFISSIONAL
from apps.administrationroute.models import AdministrationRoute  #Importa o modelo VIA DE ADMINISTRAÇÃO

# Modelo para atendimentos (sessões de vacinação)
class Session(models.Model):
    session_date = models.DateField('Data do Atendimento')
    clinic = models.ForeignKey(
        Clinic,
        verbose_name='Clínica',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    patient = models.ForeignKey(
        Person,
        verbose_name='Paciente',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    vaccines = models.ManyToManyField(Vaccine, verbose_name='Vacinas', blank=True)  # Pode conter várias vacinas
    professional = models.ForeignKey(
        Professional,
        verbose_name='Profissional',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )  # Profissional responsável pelo atendimento
    administration_route = models.ForeignKey(
        AdministrationRoute,
        verbose_name='Via de administração',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )  # Via de administração utilizada

    class Meta:
        db_table = 'CORE_SESSION'

    def __str__(self):
        clinic_name = self.clinic.name if self.clinic else "Sem clínica"
        patient_name = self.patient.name if self.patient else "Sem paciente"
        return f"Atendimento em {self.session_date} - {clinic_name} - {patient_name}"
