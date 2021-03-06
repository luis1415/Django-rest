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


class SimpleGame(models.Model):
    """
    This class is for test the API with the frontend
    """
    id = models.IntegerField(primary_key=True)
    name_player_1 = models.CharField(max_length=32)
    name_player_2 = models.CharField(max_length=32)
    move_player_1 = models.CharField(max_length=1)
    move_player_2 = models.CharField(max_length=1)
    winner = models.CharField(max_length=32)


class GamersDB(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    id_game = models.IntegerField(auto_created=True, null=True)
    player_1 = models.CharField(max_length=32)
    player_2 = models.CharField(max_length=32)


class RoundsDB(models.Model):
    """
    This class is for test the API with the frontend
    """
    id = models.IntegerField(primary_key=True)
    name_player_1 = models.CharField(max_length=32)
    name_player_2 = models.CharField(max_length=32)
    move_player_1 = models.CharField(max_length=1)
    move_player_2 = models.CharField(max_length=1)
    winner = models.CharField(max_length=32, null=True)
    round_1 = models.CharField(max_length=32, null=True)
    round_2 = models.CharField(max_length=32, null=True)
    round_3 = models.CharField(max_length=32, null=True)
