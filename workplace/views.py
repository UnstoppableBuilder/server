from rest_framework import viewsets

from workplace.models import Workplace
from workplace.serializers import WorkplaceSerializer


# Create your views here.
class WorkplaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer
