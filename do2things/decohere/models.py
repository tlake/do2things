from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Decoherence(models.Model):
    state1 = models.CharField(max_length=127)
    state2 = models.CharField(max_length=127)
    date_created = models.DateTimeField(auto_now_add=True)
    decohered = models.CharField(max_length=127, blank=True)

    objects = models.Manager

    def __str__(self):
        return 'Decoherence at {}'.format(self.date_created)
