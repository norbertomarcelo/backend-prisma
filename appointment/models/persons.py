from django.db import models


class Person(models.Model):
    name = models.CharField(
        verbose_name='Nome',
        max_length=128
    )
    cpf = models.CharField(
        verbose_name='CPF',
        max_length=11,
        unique=True
    )
    phone_number = models.CharField(
        verbose_name='Telefone',
        max_length=14,
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name='E-mail',
        null=True,
        blank=True
    )
    crated_at = models.DateField(
        verbose_name='Criado em',
        blank=True,
        auto_now_add=True
    )
    updated_at = models.DateField(
        verbose_name='Atualizado em',
        blank=True,
        auto_now=True
    )
    deleted_at = models.DateField(
        verbose_name='Deletado em',
        null=True,
    )

    class Meta:
        abstract: True

    def __str__(self):
        return self.name


class Prescriber (Person):
    coffito = models.CharField(
        verbose_name='Registro',
        max_length=14
    )

    class Meta:
        verbose_name = 'Fisioterapeuta'
        verbose_name_plural = 'Fisioterapeutas'


class Patient(Person):
    CIVIL_STATUS = (
        ('S', 'Single'),
        ('M', 'Married')
    )

    birth_date = models.DateField(
        verbose_name='Data de nascimento',
        null=True
    )
    occupations = models.TextField(
        verbose_name='Ocupação',
    )
    civil_status = models.CharField(
        verbose_name='Status civil',
        max_length=1,
        choices=CIVIL_STATUS,
        default='S'
    )
    pathologies = models.TextField(
        verbose_name='Patologias',
        null=True,
        blank=True,
    )
    address = models.ForeignKey(
        'Address',
        on_delete=models.SET_NULL,
        verbose_name='Endereço',
        null=True
    )

    def model_callable(self):
        return self.address

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


class Address(models.Model):
    public_area = models.CharField(
        verbose_name='Logradouro',
        max_length=10,
        null=False,
        blank=True
    )
    name = models.CharField(
        verbose_name='Nome',
        max_length=128
    )
    number = models.CharField(
        verbose_name='Número',
        max_length=10
    )
    district = models.CharField(
        verbose_name='Bairro',
        max_length=128
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
