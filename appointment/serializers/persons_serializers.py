from rest_framework import serializers
from appointment.models.persons import Prescriber, Patient, Address

class PrescriberSerializer(serializers.Serializer):
    class Meta:
        model = Prescriber
        fields = '__all__'

class PatientSerializer(serializers.Serializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AddressSerializer(serializers.Serializer):
    class Meta:
        model = Address
        fields = '__all__'