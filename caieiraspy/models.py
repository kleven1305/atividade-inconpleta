from django.db import models

class Caieiras(models.Model):
    nome = models.CharField(
        max_length=255,
    )

nome_musica = models.IntegerField()
nome_cantor = models.IntegerField()
genero_musical = models.IntegerField()