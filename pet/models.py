from django.db import models
from django.core.exceptions import PermissionDenied

class Pet(models.Model):
     alive     = models.BooleanField(default=True)
     name      = models.CharField(max_length=80)
     birthDate = models.DateField(auto_now_add=True)
     fedLast   = models.DateTimeField(null=True, blank=True)

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

