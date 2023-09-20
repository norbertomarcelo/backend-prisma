from django.db import models


class Assessment(models.Model):
    patient = models.ForeignKey(
        'Patient',
        on_delete=models.SET_NULL,
        verbose_name='Paciente',
        null=True
    )
    prescriber = models.ForeignKey(
        'Prescriber',
        on_delete=models.SET_NULL,
        verbose_name='Fisioterapeuta',
        null=True
    )
    date = models.DateField(
        verbose_name='Data',
        blank=True,
        auto_now_add=True
    )
    return_date = models.DateField(
        verbose_name='Próxima avaliação',
        null=True
    )

    class Meta:
        abstract: True

    def model_callable(self):
        return self.patient, self.prescriber


class Evaluation(Assessment):
    blood_pressure = models.CharField(
        verbose_name='Pressão arterial',
        max_length=10,
        null=True
    )
    spo2 = models.IntegerField(
        verbose_name='Saturação(SPO2)',
        null=True
    )
    heart_rate = models.IntegerField(
        verbose_name='Frequência cardíaca',
        null=True
    )
    respiratory_rate = models.IntegerField(
        verbose_name='Frequência respiratória',
        null=True
    )
    temperature = models.FloatField(
        verbose_name='Temperatura',
        null=True
    )
    left_goniometry = models.JSONField(
        verbose_name='Goniômetro - Esquerda',
        null=True
    )
    right_goniometry = models.JSONField(
        verbose_name='Goniômetro - Direita',
        null=True
    )
    eva = models.IntegerField(
        verbose_name='Escala de dor(EVA)',
        null=True
    )
    glasgow = models.JSONField(
        verbose_name='Escala Glasgow',
        null=True
    )
    palpation = models.TextField(
        verbose_name='Palpação',
        null=True
    )

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'


class Quiz(Assessment):
    age = models.IntegerField(
        verbose_name='Idade',
        null=True
    )
    height = models.FloatField(
        verbose_name='Altura',
        null=True
    )
    weight = models.FloatField(
        verbose_name='Peso',
        null=True
    )
    goal = models.CharField(
        verbose_name='Objetivos',
        max_length=10,
        null=True
    )
    physical_activity = models.TextField(
        verbose_name='Pratica atividades fisicas? Quais?',
        null=True
    )
    medication = models.TextField(
        verbose_name='Utiliza medicação? Qual?',
        null=True
    )
    smoker = models.BooleanField(
        verbose_name='Tabagista?',
        default=False
    )
    alcoholic = models.BooleanField(
        verbose_name='Etilista?',
        default=False
    )
    hypertensive = models.BooleanField(
        verbose_name='Hipertenso?',
        default=False
    )
    diabetic = models.BooleanField(
        verbose_name='Diabético?',
        default=False
    )
    sedentary = models.BooleanField(
        verbose_name='Sedentário?',
        default=False
    )
    pain = models.TextField(
        verbose_name='Dor? Quais?',
        null=True
    )
    surgery = models.TextField(
        verbose_name='Sirurgia? Quais?',
        null=True
    )
    hpa = models.TextField(
        verbose_name='História do problema atual(HPA)',
        null=True
    )
    hpp = models.TextField(
        verbose_name='História patológica progressiva(HPP)',
        null=True
    )
    complementary_exams = models.TextField(
        verbose_name='Exames complementares',
        null=True
    )
    biggest_complaint = models.CharField(
        verbose_name='Queixa principal',
        max_length=10,
        null=True
    )
    family_background = models.TextField(
        verbose_name='Antecedentes familiares',
        null=True
    )
    habits = models.TextField(
        verbose_name='Hábitos',
        null=True
    )

    class Meta:
        verbose_name = 'Questionário'
        verbose_name_plural = 'Questionários'
