from rest_framework import serializers

from workplace.models import Workplace, Zone


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ['id', 'name']


class WorkplaceSerializer(serializers.ModelSerializer):
    zones = ZoneSerializer(many=True)
    worker_count = serializers.IntegerField()

    class Meta:
        model = Workplace
        fields = ['id', 'name', 'address', 'zones', 'contract', 'squares', 'customer', 'contractor', 'worker_count']
