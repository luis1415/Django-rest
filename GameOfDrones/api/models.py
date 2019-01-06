from django.db import models


# Create your models here.
class PlayerDB(models.Model):
    name = models.CharField(max_length=32)
    game = models.CharField(max_length=10)
    round_1 = models.CharField(max_length=32)
    round_2 = models.CharField(max_length=32)
    round_3 = models.CharField(max_length=32)


class GameDB(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    player_1 = models.CharField(max_length=32)
    player_2 = models.CharField(max_length=32)
    winner = models.CharField(max_length=32)
