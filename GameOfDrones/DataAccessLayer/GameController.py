from GameOfDrones.Game import Game
from GameOfDrones.api.models import GameDB


class GameControler(object):
    """"
    This class control the game and save the results in the database
    """
    def __init__(self):
        self.game_list = dict()

    def add_game(self, game):
        if isinstance(Game, game):
            self.game_list[game.id] = game
        else:
            print('the game cannot be carried out')

    def game_to_db(self, id_):
        game_ = self.game_list[id_]
        if game_.is_done:
            player_1 = game_.player_1.name
            player_2 = game_.player_2.name
            winner = game_.winner

            g = GameDB(id=id_, player_1=player_1, player_2=player_2, winner=winner)
            g.save()

        else:
            print('the game cannot be carried out')
