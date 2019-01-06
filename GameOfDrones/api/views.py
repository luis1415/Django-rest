from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import PlayerSerializer
from .models import PlayerDB


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = PlayerSerializer
