from django.contrib import admin

from worker.models import Specialization, Worker, Sos, Tracking, Session
from worker.forms import TrackingForm


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    pass


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    pass


@admin.register(Tracking)
class TrackingAdmin(admin.ModelAdmin):
    form = TrackingForm


@admin.register(Sos)
class SosAdmin(admin.ModelAdmin):
    pass


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    pass
