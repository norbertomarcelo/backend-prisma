from rest_framework import serializers
from appointment.models.persons import Prescriber, Patient, Address
from appointment.validators import *


class PrescriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescriber
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
