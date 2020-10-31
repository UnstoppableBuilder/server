from django.contrib.gis.db import models


class Workplace(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Zone(models.Model):
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE, related_name='zones')
    name = models.CharField(max_length=255, null=False, blank=False)
    poly = models.PolygonField()

    def __str__(self):
        return "%s (%s)" % (self.name, self.workplace.name)
