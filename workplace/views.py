from django.contrib.gis.geos.collections import MultiPolygon
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from workplace.models import Workplace, Zone
from workplace.serializers import WorkplaceSerializer
from worker.models import Tracking


# Create your views here.
class WorkplaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Workplace.objects.all().annotate(
        worker_count=Count('sessions__worker', distinct=True)
    )
    serializer_class = WorkplaceSerializer

    def reverse_coords(self, arr):
        na = []
        for a in arr:
            if len(a) == 2 and isinstance(a[0], float):
                na.append([a[1], a[0]])
            else:
                na.append(self.reverse_coords(a))
        return na

    @action(detail=True, methods=['get'])
    def zones(self, request, pk=None):
        rows = Zone.objects.filter(workplace_id=pk)
        pols = [zone.poly for zone in rows]
        mp = MultiPolygon(pols)
        zones = [p.coords[0] for p in pols]

        wp = Workplace.objects.get(pk=pk)
        trs = Tracking
        return Response({
            "coords": self.reverse_coords(zones),
            "center": [mp.centroid.coords[1], mp.centroid.coords[0]]
        })

    @action(detail=True, methods=['get'])
    def worker_points(self, request, pk=None):

        return Response({})
