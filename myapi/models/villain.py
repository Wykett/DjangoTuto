from django.db import models


class VillainModel(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
