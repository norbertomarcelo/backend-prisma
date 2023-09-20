from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from appointment.viewsets.persons_viewset import PrescriberViewSet, PatientViewSet, AddressViewSet
from appointment.viewsets.assessments_viewset import EvaluationViewSet, QuizViewSet
from appointment.viewsets.evolutions_viewset import EvolutionViewSet, ConductViewSet

router = routers.DefaultRouter()
router.register('prescriber', PrescriberViewSet)
router.register('patient', PatientViewSet)
router.register('address', AddressViewSet)
router.register('evaluation', EvaluationViewSet)
router.register('quiz', QuizViewSet)
router.register('evolution', EvolutionViewSet)
router.register('conduct', ConductViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
