from django.contrib import admin
from appointment.models.persons import Prescriber, Patient, Address


class PrescriberAdmin(admin.ModelAdmin):
    fields = (
        'name', 'cpf', 'coffito', 'phone_number', 'email'
    )
    list_display = (
        'id', 'name', 'cpf', 'coffito', 'phone_number', 'email', 'crated_at', 'updated_at'
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
        'id', 'name', 'cpf', 'phone_number', 'email', 'crated_at', 'updated_at'
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


admin.site.register(Prescriber, PrescriberAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Address, AddressAdmin)
