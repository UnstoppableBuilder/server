from django.contrib import admin

from workplace.models import Workplace, Zone
from workplace.forms import ZoneForm


@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    form = ZoneForm
