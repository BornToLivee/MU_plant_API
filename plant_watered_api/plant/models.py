from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    species = models.CharField(max_length=255)
    water_frequency_days = models.IntegerField()
    last_watered_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
