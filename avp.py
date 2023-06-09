from exceptions import GameplayException
from connect4 import Connect4
from randomagent import RandomAgent
from minmaxagent import MinMaxAgent
from alfabetaagent import AlfaBetaAgent

connect4 = Connect4(width=7, height=6)
# CHANGE AGENT TYPE BELOW (you can change the depth too)
# agent = MinMaxAgent('x', 6)
# agent = RandomAgent('x')
agent = AlfaBetaAgent('x', 6)

while not connect4.game_over:
    connect4.draw()
    try:
        if connect4.who_moves == agent.my_token:
            n_column = agent.decide(connect4)
        else:
            n_column = int(input('Your turn: '))

        connect4.drop_token(n_column)

    except (ValueError, GameplayException):
        print('invalid move')

connect4.draw()
