from django.db import models

# Modelo para tipos de vacinas
class Type(models.Model):
    description = models.CharField('Descrição', max_length=100)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['description']  # Ordenação padrão por descrição

    def __str__(self):
        return str(self.description)


# Modelo para fornecedores de vacinas
class Supplier(models.Model):
    name = models.CharField('Nome', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=18, blank=True, null=True)
    address = models.TextField('Endereço', blank=True, null=True)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['name']  # Ordenação padrão por nome

    def __str__(self):
        return str(self.name)


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

    class Meta:
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'
        ordering = ['name']  # Ordenação por nome

    def __str__(self):
        return str(self.name)


# Modelo para pessoas (pacientes)
class Person(models.Model):
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    birth_date = models.DateField('Data de nascimento', blank=True, null=True)
    address = models.TextField('Endereço', blank=True, null=True)
    phone = models.CharField('Telefone', max_length=20, blank=True, null=True)
    email = models.EmailField('E-mail', blank=True, null=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['name']  # Ordenação por nome

    def __str__(self):
        return str(self.name)


# Modelo para clínicas
class Clinic(models.Model):
    name = models.CharField('Nome', max_length=100)
    address = models.TextField('Endereço', blank=True, null=True)
    phone = models.CharField('Telefone', max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'Clínica'
        verbose_name_plural = 'Clínicas'
        ordering = ['name']  # Ordenação por nome

    def __str__(self):
        return str(self.name)


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

    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'
        ordering = ['session_date']  # Ordenação por data

    def __str__(self):
        clinic_name = self.clinic.name if self.clinic else "Sem clínica"
        patient_name = self.patient.name if self.patient else "Sem paciente"
        return f"Atendimento em {self.session_date} - {clinic_name} - {patient_name}"
