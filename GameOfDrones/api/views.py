from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import PlayerSerializer, SimpleGameSerializer
from .models import PlayerDB, SimpleGame
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
