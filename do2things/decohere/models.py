from django.db import models


class TwoThings(models.Model):
    thing_1 = models.CharField(max_length=127)
    thing_2 = models.CharField(max_length=127)
    # created = models.DateTimeField(auto_add_now=True)
