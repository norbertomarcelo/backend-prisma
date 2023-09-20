from rest_framework import viewsets
from appointment.serializers.evolutions_serializer import EvolutionSerializer, ConductSerializer
from appointment.models.evolutions import Evolution, Conduct


class EvolutionViewSet(viewsets.ModelViewSet):
    queryset = Evolution.objects.all()
    serializer_class = EvolutionSerializer


class ConductViewSet(viewsets.ModelViewSet):
    queryset = Conduct.objects.all()
    serializer_class = ConductSerializer
