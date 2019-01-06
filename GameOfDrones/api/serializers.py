from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import PlayerDB


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerDB
        fields = ('name', 'game', 'round1', 'round2', 'round3')
