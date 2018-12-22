from django.db import models
from django.utils import timezone


class HeadLine(models.Model):
    url = models.URLField()
    headline = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)
