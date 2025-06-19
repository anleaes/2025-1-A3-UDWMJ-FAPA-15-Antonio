from django.db import models

class Type(models.Model):
    # Tipo de vacina, descrição curta
    description = models.CharField('Descrição', max_length=100)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.description


class Supplier(models.Model):
    name = models.CharField('Nome', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=18, blank=True, null=True)  # aceita vazio por enquanto
    address = models.TextField('Endereço', blank=True, null=True)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.name


class Vaccine(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', blank=True, null=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)  # protege tipo usado por vacinas
    doses = models.PositiveIntegerField('Número de doses', default=1)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name


class Clinic(models.Model):
    name = models.CharField('Nome', max_length=100)
    address = models.TextField('Endereço', blank=True, null=True)
    phone = models.CharField('Telefone', max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'Clínica'
        verbose_name_plural = 'Clínicas'

    def __str__(self):
        return self.name


class Vaccination(models.Model):
    vaccination_date = models.DateField('Data da vacinação')
    clinic = models.ForeignKey(Clinic, on_delete=models.PROTECT)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Vacinação'
        verbose_name_plural = 'Vacinações'
        ordering = ['-vaccination_date']

    def __str__(self):
        return f"{self.person.name} - {self.vaccination_date}"


class VaccineItem(models.Model):
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.PROTECT)
    vaccination = models.ForeignKey(Vaccination, on_delete=models.CASCADE, related_name='items')

    class Meta:
        verbose_name = 'Item de Vacina'
        verbose_name_plural = 'Itens de Vacina'

    def __str__(self):
        return f"{self.vaccine.name} - {self.quantity}"


class Session(models.Model):
    session_date = models.DateField('Data da sessão')
    vaccine_item = models.ForeignKey(VaccineItem, on_delete=models.CASCADE, related_name='sessions')

    class Meta:
        verbose_name = 'Sessão'
        verbose_name_plural = 'Sessões'

    def __str__(self):
        return f"Sessão em {self.session_date}"