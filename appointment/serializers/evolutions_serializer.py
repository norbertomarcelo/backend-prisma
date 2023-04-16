from rest_framework import serializers
from appointment.models.evolutions import Evolution, Conduct


class EvolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evolution
        fields = '__all__'


class ConductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conduct
        fields = '__all__'
