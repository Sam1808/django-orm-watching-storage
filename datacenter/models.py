from django.db import models
from django.utils import timezone


def format_duration(duration):
    decimal_duration = duration.total_seconds() / 3600
    hours = int(decimal_duration)
    minutes = int((decimal_duration - hours) * 60)
    if minutes < 10:
        minutes = '0' + str(minutes)
    formated_duration = f'{hours} hours {minutes} minutes'
    return formated_duration

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
    def get_duration(visit):
        if visit.leaved_at == None:
            current_time = timezone.now()
            total_time = current_time - visit.entered_at
            return total_time
        total_time = visit.leaved_at - visit.entered_at
        return total_time

    def is_visit_long(visit, minutes=60):
        visit_time = visit.get_duration()
        visit_time = visit_time.total_seconds() /60
        return visit_time >= minutes


