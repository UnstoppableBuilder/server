from django.contrib.gis.db import models


class Workplace(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название")
    address = models.TextField(blank=True, null=True, verbose_name="Адрес")
    contract = models.CharField(max_length=255, null=True, blank=True, verbose_name="Контракт")
    squares = models.CharField(max_length=255, null=True, blank=True, verbose_name="Площадь")
    customer = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заказчик")
    contractor = models.CharField(max_length=255, null=True, blank=True, verbose_name="Подрядчик")

    class Meta:
        verbose_name = 'Объект строительства'
        verbose_name_plural = 'Объекты строительства'

    def __str__(self):
        return self.name


class Zone(models.Model):
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE, related_name='zones', verbose_name="Объект строительства")
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название")
    poly = models.PolygonField(verbose_name="Координаты")

    class Meta:
        verbose_name = 'Зона'
        verbose_name_plural = 'Зоны'

    def __str__(self):
        return "%s (%s)" % (self.name, self.workplace.name)
