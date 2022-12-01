from datetime import date

from django.db import models


class Apostas(models.Model):
    concurso = models.CharField(max_length=8)
    num_selected = models.TextField(null=True, blank=True)
    data = models.DateField(default=date.today)

    class Meta:
        verbose_name = 'Aposta'

    def __str__(self) -> str:
        return self.concurso
