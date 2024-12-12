
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Partida(models.Model):
    jogador = models.ForeignKey(User, on_delete=models.CASCADE)
    tentativas = models.IntegerField()
    tempo = models.DurationField(blank=True, null=True)
    data_hora = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.jogador.username} - {self.tentativas} tentativas"
