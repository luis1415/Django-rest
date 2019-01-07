from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import PlayerSerializer, SimpleGameSerializer, GamersSerializer, RoundsSerializer
from .models import PlayerDB, SimpleGame, GamersDB, RoundsDB
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PlayerDB.objects.all()
    serializer_class = PlayerSerializer


class SimpleGameList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        games = SimpleGame.objects.all()
        serializer = SimpleGameSerializer(games, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        serializer = SimpleGameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SimpleGameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SimpleGame.objects.all()
    serializer_class = SimpleGameSerializer

# Game of drones


class InitGameViewSet(viewsets.ModelViewSet):
    """
    API endpoint to initialize the game
    """
    queryset = GamersDB.objects.all().order_by('-date')
    serializer_class = GamersSerializer


class RoundViewSet(viewsets.ModelViewSet):
    """
    API endpoint to initialize the game
    """
    queryset = RoundsDB.objects.all()
    serializer_class = RoundsSerializer
