from rest_framework import viewsets, filters
from appointment.serializers.persons_serializers import PrescriberSerializer, PatientSerializer
from appointment.models.persons import Prescriber, Patient
from django_filters.rest_framework import DjangoFilterBackend

class PrescriberViewSet(viewsets.ModelViewSet):
    queryset = Prescriber.objects.all()
    serializer_class = PrescriberSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    ordering_fields = ['nome', 'coffito']

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    ordering_fields = ['nome', 'cpf']