from django.contrib.auth.models import User
from django.contrib.gis.db import models

from workplace.models import Workplace, Zone


class Specialization(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.name


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="worker")
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    phone = models.CharField(max_length=15, unique=True, verbose_name="Телефон")
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT, verbose_name="Специализация")
    is_approved = models.BooleanField(default=False, verbose_name="Одобрен")

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Session(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name="Сотрудник")
    workplace = models.ForeignKey(Workplace, on_delete=models.PROTECT, related_name='sessions', verbose_name="Сессия")
    zone = models.ForeignKey(Zone, null=True, default=None, on_delete=models.PROTECT, verbose_name="Зона")
    started_at = models.DateTimeField(verbose_name="Начал")
    ended_at = models.DateTimeField(null=True, db_index=True, verbose_name="Закончил")

    class Meta:
        verbose_name = 'Рабочая сессия'
        verbose_name_plural = 'Рабочие сессии'

    def __str__(self):
        return "%s (%s): %s" % (self.worker, self.workplace, self.started_at)


class Tracking(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name="Сотрудник")
    session = models.ForeignKey(Session, on_delete=models.CASCADE, verbose_name="Сессия")
    gps = models.PointField(verbose_name="Место")
    noise_level = models.FloatField(null=True, verbose_name="Уровень шума")
    light_level = models.FloatField(null=True, verbose_name="Уровень света")
    acceleration = models.JSONField(null=True, verbose_name="Движения")
    created_at = models.DateTimeField(verbose_name="Дата")

    class Meta:
        verbose_name = 'Трэкинг'
        verbose_name_plural = 'Трэкинг'

    def __str__(self):
        return "%s (%s)" % (self.worker, self.created_at)


class Sos(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, verbose_name="Сессия")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    class Meta:
        verbose_name = 'SOS'
        verbose_name_plural = 'SOS'

    def __str__(self):
        return "#%s %s (%s)" % (self.id, self.session.workplace, self.session.worker, )
