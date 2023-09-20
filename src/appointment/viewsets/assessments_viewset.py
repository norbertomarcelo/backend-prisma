from rest_framework import viewsets
from appointment.serializers.assessments_serializer import EvaluationSerializer, QuizSerializer
from appointment.models.assessments import Evaluation, Quiz


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
