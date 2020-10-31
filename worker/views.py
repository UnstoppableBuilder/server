from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from worker.models import Session, Specialization, Sos, Tracking
from worker.permissions import IsAuthenticated
from worker.serializers import SessionSerializer, SpecializationSerializer, SignupSerializer, \
    SosSerializer, WorkerSerializer, TrackingSerializer


class SpecializationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class AuthToken(viewsets.ViewSet):
    serializer_class = SignupSerializer

    def list(self, request):
        return Response({
            'token': request.user.auth_token.key,
            'worker': WorkerSerializer(request.user.worker).data
        })

    def create(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        worker = serializer.validated_data['worker']
        token, created = Token.objects.get_or_create(user=worker.user)

        return Response({
            'token': token.key,
            'worker': WorkerSerializer(worker).data
        })

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


class WorkerViewSet(viewsets.ViewSet):
    serializer_class = WorkerSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return Response(WorkerSerializer(request.user.worker).data)

    @action(detail=False, methods=['post'])
    def sos(self, request):
        serializer = SosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sos = Sos.objects.create(
            session=serializer.validated_data["session_id"],
            description=serializer.validated_data["description"],
            created_at=serializer.validated_data.get("created_at")
        )
        return Response(SosSerializer(sos).data)

    @action(detail=False, methods=['post'])
    def track(self, request):
        serializer = TrackingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tracking = Tracking.objects.create(
            worker=request.user.worker,
            session=serializer.validated_data["session_id"],
            gps=serializer.validated_data["gps"],
            noise_level=serializer.validated_data.get("noise_level"),
            light_level=serializer.validated_data.get("light_level"),
            acceleration=serializer.validated_data.get("acceleration"),
            created_at=serializer.validated_data.get("created_at")
        )
        return Response(TrackingSerializer(tracking).data)


class SessionViewSet(viewsets.ViewSet):
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        try:
            session = Session.objects.get(worker=request.user.worker, ended_at__isnull=True)
            return Response(self.serializer_class(session).data)
        except Session.DoesNotExist:
            raise NotFound()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            session = Session.objects.get(worker=request.user.worker, ended_at__isnull=True)
        except Session.DoesNotExist:
            session = Session.objects.create(
                worker=request.user.worker,
                workplace=serializer.validated_data["workplace_id"],
                zone=serializer.validated_data["zone_id"],
                started_at=serializer.validated_data["started_at"],
            )

        session.ended_at = serializer.validated_data["ended_at"]
        session.save()
        return Response(self.serializer_class(session).data)
