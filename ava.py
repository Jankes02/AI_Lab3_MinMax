from exceptions import GameplayException
from connect4 import Connect4
from randomagent import RandomAgent
from minmaxagent import MinMaxAgent
from alfabetaagent import AlfaBetaAgent

connect4 = Connect4(width=7, height=6)
# CHANGE AGENT TYPES BELOW (you can change the depth too)
# agentX = MinMaxAgent('x', 6)
# agentX = RandomAgent('x')
agent1 = AlfaBetaAgent('o', 6)
agent2 = AlfaBetaAgent('x', 6)

while not connect4.game_over:
    connect4.draw()
    try:
        if connect4.who_moves == agent1.my_token:
            n_column = agent1.decide(connect4)
        else:
            n_column = agent2.decide(connect4)

        connect4.drop_token(n_column)

    except (ValueError, GameplayException):
        print('invalid move')

connect4.draw()
