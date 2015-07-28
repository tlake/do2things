# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Decoherence(models.Model):
    state1 = models.CharField(max_length=127)
    state2 = models.CharField(max_length=127)
    date_created = models.DateTimeField(auto_now_add=True)
    decohered = models.CharField(max_length=127, blank=True)

    def __str__(self):
        return 'Decoherence at {}'.format(self.date_created)
