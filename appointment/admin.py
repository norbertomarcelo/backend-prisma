from django.contrib import admin
from appointment.models.persons import Prescriber, Patient, Address
from appointment.models.assessments import Evaluation, Quiz
from appointment.models.evolutions import Evolution, Conduct


class PrescriberAdmin(admin.ModelAdmin):
    fields = (
        'name', 'cpf', 'coffito', 'phone_number', 'email'
    )
    list_display = (
        'id', 'name', 'cpf', 'coffito', 'phone_number', 'email', 'created_at', 'updated_at'
    )
    search_fields = (
        'name', 'cpf', 'coffito', 'phone_number', 'email'
    )
    list_per_page = 10


class PatientAdmin(admin.ModelAdmin):

    fields = (
        'name', 'cpf', 'phone_number', 'email', 'birth_date', 'occupations',
        'civil_status', 'pathologies', 'address'
    )
    list_display = (
        'id', 'name', 'cpf', 'phone_number', 'email', 'created_at', 'updated_at'
    )
    search_fields = (
        'name', 'cpf', 'phone_number', 'email'
    )
    list_per_page = 10
    autocomplete_fields = ('address',)


class AddressAdmin(admin.ModelAdmin):
    fields = (
        'public_area', 'name', 'number', 'district'
    )
    list_display = (
        'id', 'public_area', 'name', 'number', 'district'
    )
    search_fields = (
        'public_area', 'name', 'number', 'district'
    )
    list_per_page = 10


class EvaluationAdmin(admin.ModelAdmin):
    fields = (
        'patient', 'prescriber', 'blood_pressure', 'spo2', 'heart_rate',
        'respiratory_rate', 'temperature', 'left_goniometry', 'right_goniometry',
        'eva', 'glasgow', 'palpation', 'return_date'
    )
    list_display = (
        'patient', 'prescriber', 'date'
    )
    search_fields = (
        'patient', 'prescriber', 'date'
    )
    list_per_page = 10
    autocomplete_fields = (
        'patient', 'prescriber'
    )


class QuizAdmin(admin.ModelAdmin):
    fields = (
        'patient', 'prescriber', 'age', 'birth_date', 'height', 'weight', 'goal',
        'physical_activity', 'medication', 'smoker', 'alcoholic', 'hypertensive',
        'diabetic', 'sedentary', 'pain', 'surgery', 'hpa', 'hpp',
        'complementary_exams', 'biggest_complaint', 'family_background', 'habits',
        'return_date'
    )
    list_display = (
        'patient', 'prescriber', 'date'
    )
    search_fields = (
        'patient', 'prescriber', 'date'
    )
    list_per_page = 10
    autocomplete_fields = (
        'patient', 'prescriber'
    )


class EvolutionAdmin(admin.ModelAdmin):
    fields = (
        'patient', 'prescriber', 'header', 'description'
    )
    list_display = (
        'patient', 'prescriber', 'header', 'date'
    )
    search_fields = (
        'patient', 'prescriber', 'header', 'date'
    )
    list_per_page = 10
    autocomplete_fields = (
        'patient', 'prescriber'
    )


class ConductAdmin(admin.ModelAdmin):
    fields = (
        'evolution', 'header', 'description'
    )
    list_display = (
        'evolution', 'header', 'date'
    )
    search_fields = (
        'evolution', 'header', 'date'
    )
    list_per_page = 10
    autocomplete_fields = (
        'evolution',
    )


admin.site.register(Prescriber, PrescriberAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Evaluation, EvaluationAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Evolution, EvolutionAdmin)
admin.site.register(Conduct, ConductAdmin)
