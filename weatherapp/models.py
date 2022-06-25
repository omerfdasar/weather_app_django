from django.db import models


class City(models.Model):
    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
