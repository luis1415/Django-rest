class Game(object):
    """
    This class controls a game and takes the logic to decide who wins
    """
    def __init__(self, id_, player1, player2):
        self.id = id_
        self.player1 = player1
        self.player2 = player2
        self.is_done = False
        self.winner = None

    def set_winner(self):
        self.set_is_done()
        if self.is_done:
            total_score_player_1 = sum([getattr(self.player1, "score_" + str(i)) for i in range(1, 4)])
            total_score_player_2 = sum([getattr(self.player2, "score_" + str(i)) for i in range(1, 4)])
            results = {total_score_player_1: self.player1.name,
                       total_score_player_2: self.player2.name,
                       }
            self.winner = results[max(results.keys())]
        else:
            print('the game is not done')

    def set_is_done(self):
        self.in_done = self.player1.score_3 is not None and self.player2.score_3 is not None
