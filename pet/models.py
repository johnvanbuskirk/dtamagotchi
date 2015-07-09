from django.db import models
from django.core.exceptions import PermissionDenied
from django.utils import timezone


class Pet(models.Model):
    alive = models.BooleanField(default=True)
    name = models.CharField(max_length=80)
    birth_date = models.DateField(auto_now_add=True)
    last_fed = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __unicode__(self):
        return ("%s is %s and was born on %s") % (self.name, "alive" if self.alive else "dead". str(self.date))

    def __init__(self, *args, **kwargs):
        super(Pet, self).__init__(*args, **kwargs)
        self._was_alive = self.alive

    def save(self, *args, **kwargs):
        if (not self._was_alive):
            raise PermissionDenied
        else:
            return super(Pet, self).save(*args, **kwargs)

    @property
    def neglected(self, *args, **kwargs):
        delta = self.last_fed - timezone.now()
        if delta.total_seconds() <= -86400:
            return True
        else:
            return False