from datetime import datetime

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_gis.fields import GeometryField

from worker.models import Session, Sos, Specialization, Tracking, Worker
from workplace.models import Workplace, Zone


class SpecializationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id', 'name']


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['first_name', 'last_name', 'specialization_id']


class SignupSerializer(serializers.Serializer):
    phone = serializers.CharField(label="Телефон", write_only=True, required=True)
    code = serializers.CharField(label="Код", write_only=True, required=True)
    first_name = serializers.CharField(label="Имя", write_only=True)
    last_name = serializers.CharField(label="Фамилия", write_only=True)
    specialization_id = serializers.PrimaryKeyRelatedField(
        queryset=Specialization.objects, label="Специализация", write_only=True
    )

    access_token = serializers.CharField(
        label="Токен",
        read_only=True
    )
    worker = WorkerSerializer(read_only=True, many=False)

    def validate(self, attrs):
        phone = attrs.get("phone")
        code = attrs.get("code")

        try:
            worker = Worker.objects.get(phone=phone)
        except Worker.DoesNotExist:
            first_name = attrs.get("first_name")
            last_name = attrs.get("last_name")
            specialization_id = attrs.get("specialization_id")

            if not first_name or not last_name or not specialization_id:
                raise serializers.ValidationError("names and specialization required for new worker",
                                                  code='authorization')

            user = User.objects.create(
                username=phone,
                first_name=first_name,
                last_name=last_name
            )

            worker = Worker.objects.create(
                user=user,
                phone=phone,
                specialization=specialization_id,
                first_name=first_name,
                last_name=last_name
            )

        attrs["worker"] = worker
        return attrs


class TimestampField(serializers.DateTimeField):
    """
    Convert a django datetime to/from timestamp.
    """
    def to_representation(self, value):
        """
        Convert the field to its internal representation (aka timestamp)
        :param value: the DateTime value
        :return: a UTC timestamp integer
        """
        # result = super(TimestampField, self).to_representation(value)
        return value.timestamp()

    def to_internal_value(self, value):
        """
        deserialize a timestamp to a DateTime value
        :param value: the timestamp value
        :return: a django DateTime value
        """
        converted = datetime.fromtimestamp(float('%s' % value))
        return converted


class SessionSerializer(serializers.ModelSerializer):
    started_at = TimestampField()
    ended_at = TimestampField(allow_null=True)
    workplace_id = serializers.PrimaryKeyRelatedField(queryset=Workplace.objects)
    zone_id = serializers.PrimaryKeyRelatedField(queryset=Zone.objects, allow_null=True, required=False)

    class Meta:
        model = Session
        fields = ['id', 'worker_id', 'workplace_id', 'zone_id', 'started_at', 'ended_at']
        read_only_fields = ['id', 'worker_id']


class SosSerializer(serializers.ModelSerializer):
    session_id = serializers.PrimaryKeyRelatedField(queryset=Session.objects)
    created_at = TimestampField(allow_null=True, required=False)

    class Meta:
        model = Sos
        fields = ['id', 'session_id', 'description', 'created_at']
        read_only_fields = ['id',]


class TrackingSerializer(serializers.ModelSerializer):
    worker_id = serializers.PrimaryKeyRelatedField(queryset=Worker.objects, allow_null=True, required=False)
    session_id = serializers.PrimaryKeyRelatedField(queryset=Session.objects, required=False)
    created_at = TimestampField(allow_null=True, required=False)
    gps = GeometryField()

    class Meta:
        model = Tracking
        fields = ['id', 'worker_id', 'session_id', 'gps', 'noise_level', 'light_level', 'acceleration', 'created_at']
        read_only_fields = ['id', 'worker_id']
