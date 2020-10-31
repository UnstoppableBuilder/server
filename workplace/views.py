from django.db.models import Count
from rest_framework import viewsets

from workplace.models import Workplace
from workplace.serializers import WorkplaceSerializer


# Create your views here.
class WorkplaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Workplace.objects.all().annotate(
        worker_count=Count('sessions__worker', distinct=True)
    )
    serializer_class = WorkplaceSerializer
