from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=200, null=False)
    population = models.IntegerField(null=True)
    terrains = models.CharField(max_length=200, null=True)
    climates = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
