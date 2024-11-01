from datetime import datetime, timedelta

from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    species = models.CharField(max_length=255)
    water_frequency_days = models.IntegerField()
    last_watered_date = models.DateField(null=True, blank=True)

    @property
    def is_watered(self):
        if not self.last_watered_date:
            return False
        return (datetime.now().date() - self.last_watered_date) < timedelta(
            days=self.water_frequency_days
        )

    def __str__(self):
        return self.name
