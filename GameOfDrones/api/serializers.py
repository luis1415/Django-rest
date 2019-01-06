from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import PlayerDB, SimpleGame, GamersDB


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerDB
        fields = ('name', 'game', 'round_1', 'round_2', 'round_3')


class SimpleGameSerializer(serializers.ModelSerializer):
    """
    Sample to save a object using the serializer
    """
    class Meta:
        model = SimpleGame
        fields = ('id', 'name_player_1', 'name_player_2', 'move_player_1', 'move_player_2', 'winner')

    def create(self, validated_data):
        id_ = validated_data.get('id')
        name_player_1 = validated_data.get('name_player_1')
        name_player_2 = validated_data.get('name_player_2')
        move_player_1 = validated_data.get('move_player_1')
        move_player_2 = validated_data.get('move_player_2')
        winner = ""

        if move_player_1 == move_player_2:
            winner = "Tie"
        elif move_player_1 == "r":
            if move_player_2 == "s":
                winner = name_player_1
            else:
                winner = name_player_2

        elif move_player_1 == "p":
            if move_player_2 == "r":
                winner = name_player_1
            else:
                winner = name_player_2

        elif move_player_1 == "s":
            if move_player_2 == "p":
                winner = name_player_1
            else:
                winner = name_player_2

        # save the object simple game
        game_ = SimpleGame(
            id=id_,
            name_player_1=name_player_1,
            name_player_2=name_player_2,
            move_player_1=move_player_1,
            move_player_2=move_player_2,
            winner=winner
        )

        game_.save()

        return game_


class GamersSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamersDB
        fields = ('id', 'player_1', 'player_2')
