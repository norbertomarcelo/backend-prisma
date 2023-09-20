from rest_framework import viewsets, filters
from appointment.serializers.persons_serializers import PrescriberSerializer, PatientSerializer, AddressSerializer
from appointment.models.persons import Prescriber, Patient, Address
from django_filters.rest_framework import DjangoFilterBackend


class PrescriberViewSet(viewsets.ModelViewSet):
    queryset = Prescriber.objects.all()
    serializer_class = PrescriberSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
