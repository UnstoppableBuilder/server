from django.contrib.auth.models import User
from django.contrib.gis.db import models

from workplace.models import Workplace, Zone


class Specialization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="worker")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Session(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    workplace = models.ForeignKey(Workplace, on_delete=models.PROTECT)
    zone = models.ForeignKey(Zone, null=True, default=None, on_delete=models.PROTECT)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True, db_index=True)


class Tracking(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    gps = models.PointField()
    noise_level = models.FloatField(null=True)
    light_level = models.FloatField(null=True)
    acceleration = models.JSONField(null=True)
    created_at = models.DateTimeField()


class Sos(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
