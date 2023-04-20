import connect4
import copy
import random
import math
from exceptions import AgentException


class MinMaxAgent:
    def __init__(self, token='x', depth=6):
        self.depth = depth
        self.my_token = token

    def decide(self, game=connect4.Connect4()):  # returns int - # of columns
        if game.who_moves != self.my_token:
            raise AgentException('not my round')

        move = self.minmax(game=game, depth=self.depth, maximizing_player=True)
        if move is None:
            return random.choice(game.possible_drops())

        return move[0]

    def minmax(self, game, depth, maximizing_player):
        if game.check_game_over():
            if game.wins is None:             # TIE
                return None, 0
            if game.wins == self.my_token:    # AGENT WINS
                game.wins = None
                return None, 1000000
            else:                               # OPPONENT WINS
                game.wins = None
                return None, -1000000

        if depth == 0:
            if maximizing_player:
                return None, game.heuristic(self.my_token)
            else:
                return None, -game.heuristic(self.my_token)

        column = None
        valid_moves = game.possible_drops()

        if maximizing_player:
            value = -math.inf
            for col in valid_moves:
                b_copy = copy.deepcopy(game.board)
                game.drop_token_fixed(self.my_token, col)
                new_score = self.minmax(game, depth - 1, False)[1]
                game.board = b_copy
                if new_score > value:
                    value = new_score
                    column = col
            return column, value

        else:  # Minimizing player
            value = math.inf
            for col in valid_moves:
                b_copy = copy.deepcopy(game.board)
                game.drop_token_fixed(game.negate_token(self.my_token), col)
                new_score = self.minmax(game, depth - 1, True)[1]
                game.board = b_copy
                if new_score < value:
                    value = new_score
                    column = col
            return column, value
