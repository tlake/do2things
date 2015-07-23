from django.db import models


class TwoThings(models.Model):
    thing_1 = models.TextField()
    thing_2 = models.TextField()
    created = models.DateTimeField(auto_add_now=True)
