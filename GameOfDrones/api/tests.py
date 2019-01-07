from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import PlayerDB
from .views import SimpleGameList
from .serializers import PlayerSerializer
from rest_framework.test import APIRequestFactory, force_authenticate


class TestPlayers(TestCase):
    """
    Sample for testing
    """

    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.user = PlayerDB(name='user1', game='game', round_1='user1', round_2='user2', round_3='user')
        self.user._set_pk_val(1)
        self.user.save()

    def test_get_all_players(self):
        todo1 = PlayerDB(name='Luis')
        todo1.save()
        todo2 = PlayerDB(name='Juan')
        todo2.save()

        request = self.request_factory.get(reverse('players'), format='json')
        force_authenticate(request, user=self.user)
        view = SimpleGameList.as_view()
        response = view(request)
        response.render()
        players = PlayerDB.objects.all()
        serializer = PlayerSerializer(players, many=True, context={'request': request})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
